# SWEA 1767 프로세서 연결하기
# SWEA 1767

# Created by sw0817 on 2021. 03. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 검사 중인 코어, 연결된 코어 수, 전선 길이
def check(k, co, l):
    global core, length

    # 나머지 코어 다 연결해도 최대 코어 수 안 되면 버려 (매우 중요)
    if co + len(lexi) - k < core:
        return

    # 이미 모든 코어 검사한거임
    if k == len(lexi):

        # 코어 수 넘겼으면 갱신하고
        if core < co:
            core = co
            length = l

        # 같으면 전선 길이 비교
        elif core == co and l < length:
            length = l
        return

    # 사방으로 전선 연결해볼건데 하나만 연결하면 됨
    for dr, dc in move:
        # 현재 코어 위치
        r, c = lexi[k]
        # 실제로 연결 되면 연결될 전선 위치
        stack = []
        # 가장자리까지 검사하겠다는 의미고 r, c가 가장자리여서 넘어가는 값이 나오면 그 때가 연결되었다는 의미
        # 가장자리에서 멈추지 않는 이유는 stack에 담는 방식때문
        while 0 <= r < N and 0 <= c < N:
            r += dr
            c += dc
            # 배열 밖 즉 가장자리에 연결됨
            if r == -1 or c == -1 or r == N or c == N:
                # 연결된 코어 수 늘리고
                co += 1
                # 전선 길이는 stack 길이임
                s_l = len(stack)
                l += s_l
                # stack 에 담긴 위치 다 전선으로 바꿈
                for x, y in stack:
                    arr[x][y] = 2
                # 이 상태에서 다음 코어 검사
                check(k+1, co, l)
                # 전선 연결한거 다시 풀고
                for x, y in stack:
                    arr[x][y] = 0
                # 코어 수랑 전선 길이 원상복구 하면 다음 방향 검사할거임. 모든 방향 검사후엔 연결 안 된 채 다음 코어 검사
                co -= 1
                l -= s_l

            # 중간에 코어나 선이 있으면 이 방향으론 연결 불가 그냥 break 해도 stack은 알아서 초기화 함
            elif arr[r][c] == 1 or arr[r][c] == 2:
                break

            # 빈 공간이면 전선 늘리기
            else:
                stack.append((r, c))

        # 연결 안 된 채 다음 코어 검사
        check(k+1, co, l)


# 일단 재귀 쓸거임
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 7 <= N <= 12 개 작음
    arr = []
    # core 위치
    lexi = []
    core = 0
    length = 0
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                # 여기 걸리면 가장자리라서 그냥 안 세도 무방
                if i == 0 or j == 0 or i == N-1 or j == N-1:
                    core += 1
                # 다른 코어는 append
                else:
                    lexi.append((i, j))
        arr.append(row)

    check(0, core, length)
    print('#{} {}'.format(tc, length))