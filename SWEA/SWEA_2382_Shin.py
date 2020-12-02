# SWEA 2382 미생물 격리
# SWEA 2382

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl

# 속도 향상을 위해 deque을 사용
from _collections import deque


T = int(input())

direct = ['1', '2', '3', '4']  # 상하좌우

for tc in range(1, T + 1):

    # 셀의 개수 N, 격리 시간 M, 미생물 군집 수 K
    N, M, K = map(int, input().split())

    # 미생물의 상태 배열
    microbes = []

    # 각 미생물 군집의 상태
    for i in range(K):
        microbe = list(map(int, input().split()))
        microbes.append(microbe)

    # 격리 시간동안 셀의 변화를 체크한다.
    for i in range(M):
        arr = [[0] * N for _ in range(N)]
        stack = deque()

        # 미생물 군집 별로 조사한다.
        for _ in range(len(microbes)):

            # 현재 조사하는 미생물 군집
            temp = microbes.pop()

            # 이동 방향에 따라 세로나 가로 위치는 변하지 않는다.
            r = nr = temp[0]
            c = nc = temp[1]

            # 이동 방향에 따른 다음 위치
            if temp[3] == 1:
                nr = r - 1
            elif temp[3] == 2:
                nr = r + 1
            elif temp[3] == 3:
                nc = c - 1
            else:
                nc = c + 1

            # 벽에 닿으면 방향은 바뀌고 수는 반으로 줄어든다.
            if nr == 0 or nc == 0:
                temp[3] += 1
                temp[2] = temp[2] // 2

            elif nr == N - 1 or nc == N - 1:
                temp[3] -= 1
                temp[2] = temp[2] // 2

            # 미생물 수가 0이 되면 움직임에 의미가 없다.
            if temp[2] == 0:
                continue

            # 이동한 곳에 미생물이 없다면
            if arr[nr][nc] == 0:

                # 미생물의 수와 위치는 현재 정보와 같다.
                # 이때, 방향을 좌우하는 미생물의 수는 총 합이 아닌 그 방향 미생물 수
                arr[nr][nc] = [temp[2], [temp[2], temp[3]]]

                # 다음 격리 시간에 사용할 정보
                stack.append((nr, nc))

            # 이미 미생물이 있다면
            else:

                # 현재 미생물의 수가 방향을 좌우하는 미생물 수보다 더 많다면
                if arr[nr][nc][1][0] < temp[2]:

                    # 방향을 좌우하는 정보는 현재 미생물 정보
                    arr[nr][nc][1][0], arr[nr][nc][1][1] = temp[2], temp[3]

                # 총합은 기존 미생물 수 + 현재 미생물 수
                arr[nr][nc][0] += temp[2]

        # i == M-1 에서는 미생물의 수만 알면 된다.
        if i == M - 1:
            break

        # 미생물 군집이 있다면
        while stack:

            r, c = stack.pop()

            # 새로운 군집 정보를 추가해준다.
            microbes.append([r, c, arr[r][c][0], arr[r][c][1][1]])

    result = 0

    # 미생물의 수를 계산한다.
    while stack:
        r, c = stack.pop()
        result += arr[r][c][0]

    print('#{} {}'.format(tc, result))