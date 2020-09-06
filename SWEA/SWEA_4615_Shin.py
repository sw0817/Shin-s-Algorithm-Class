# SWEA 4615 재미있는 오셀로 게임
# SWEA 4615

# Created by sw0817 on 2020. 09. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj&categoryId=AWQmA4uK8ygDFAXj&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list([0]*N) for _ in range(N)]

    arr[N//2][N//2] = 2
    arr[N//2 - 1][N//2 - 1] = 2
    arr[N//2][N//2 -1] = 1
    arr[N//2 -1][N//2] = 1

    osello = [list(map(int, input().split())) for _ in range(M)]

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(M):
        x = osello[i][0]-1
        y = osello[i][1]-1
        if osello[i][2] == 2:
            arr[x][y] = 2
            for j in range(8):
                nr = x + dr[j]
                nc = y + dc[j]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                rocks = []
                while arr[nr][nc] == 1:
                    rocks.append([nr, nc])
                    nr = nr + dr[j]
                    nc = nc + dc[j]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    if arr[nr][nc] == 2:
                        for rock in rocks:
                            arr[rock[0]][rock[1]] = 2

        elif osello[i][2] == 1:
            arr[x][y] = 1
            for j in range(8):
                nr = x + dr[j]
                nc = y + dc[j]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                rocks = []
                while arr[nr][nc] == 2:
                    rocks.append([nr, nc])
                    nr = nr + dr[j]
                    nc = nc + dc[j]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    if arr[nr][nc] == 1:
                        for rock in rocks:
                            arr[rock[0]][rock[1]] = 1

    cnt1 = 0
    cnt2 = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1

    print('#{} {} {}'.format(tc, cnt1, cnt2))