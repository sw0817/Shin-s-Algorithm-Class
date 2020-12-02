# SWEA 1949 등산로 조성
# SWEA 1949

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE

# 속도 향상을 위해 deque을 사용
from _collections import deque


# 4방향 탐색을 할 것이다.
next = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 등산 함수
def goHiking(i, j):

    # 결과 값은 전역변수로 처리한다.
    global result

    # 현재 함수에서 등산로 길이
    road = 0

    queue = deque()
    queue.append((i, j))

    # BFS 사용
    while queue:

        # 현재 길이 위치 모든 곳에서
        for _ in range(len(queue)):
            r, c = queue.popleft()

            # 4방향 탐색
            for k in range(4):
                dr, dc = next[k]
                nr = r + dr
                nc = c + dc

                # 다음 길이 있다면 추가
                if 0 <= nr < N and 0 <= nc < N and roads[nr][nc] < roads[r][c]:
                    queue.append((nr, nc))

        # 현재 길이에서 모든 다음 위치를 찾았으니 길이 1 증가
        road += 1

    # 결과값 갱신
    if road > result:
        result = road


T = int(input())

for tc in range(1, T + 1):

    # 등산 범위 N, 최대 공사 깊이 K
    N, K = map(int, input().split())

    # 최고 높이
    highest = 1

    # 최고 높이 위치 배열
    highests = []

    # 등산로
    roads = []

    # 결과값
    result = 0

    # 최고 높이와 그 위치를 찾는다.
    for i in range(N):
        arr = list(map(int, input().split()))

        for j in range(N):

            if arr[j] == highest:
                highests.append((i, j))

            elif arr[j] > highest:
                highest = arr[j]
                highests = [(i, j)]

        roads.append(arr)

    # 모든 곳을 공사해본다.
    for i in range(N):
        for j in range(N):

            # 공사 깊이는 1 ~ K
            for k in range(K):

                # 1씩 공사해가며 모든 최고 높이에서 등산로 길이를 잰다.
                roads[i][j] -= 1
                for (r, c) in highests:
                    goHiking(r, c)

            # 한 위치에서 모든 공사 깊이를 조사해봤다면 다시 공사 흔적을 지운다.
            roads[i][j] += K

    print('#{} {}'.format(tc, result))