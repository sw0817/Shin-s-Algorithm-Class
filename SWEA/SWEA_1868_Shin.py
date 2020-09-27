# SWEA 1868 파핑파핑 지뢰찾기
# SWEA 1868

# Created by sw0817 on 2020. 09. 27..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LwsHaD1MDFAXc&categoryId=AV5LwsHaD1MDFAXc&categoryType=CODE


dr = [1, 1, 0, -1, -1, -1, 0, 1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def mine(i, j):
    cnt = 0
    for k in range(8):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == '*':
            cnt += 1
    G[i][j] = cnt
    return


def zero(i, j):
    stack.append((i, j))
    while stack:
        i, j = stack.pop()
        G[i][j] = 10
        for k in range(8):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] == 0:
                stack.append((nr, nc))
            if 0 <= nr < N and 0 <= nc < N and G[nr][nc] > 0 and G[nr][nc] != '*':
                G[nr][nc] = 10
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [list(input()) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    result = 0
    stack = []
    for i in range(N):
        for j in range(N):
            if G[i][j] == '.':
                mine(i, j)

    for i in range(N):
        for j in range(N):
            if G[i][j] == 0:
                zero(i, j)
                result += 1

    for i in range(N):
        for j in range(N):
            if type(G[i][j]) == int and 0 < G[i][j] < 9:
                result += 1
                
    print('#{} {}'.format(tc, result))