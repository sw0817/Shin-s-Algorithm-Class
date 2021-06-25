# 백준 1012 유기농 배추
# Baekjoon 1012

# Created by sw0817 on 2021. 06. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1012

from _collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(r, c):
    arr[r][c] = 0
    queue = deque()
    queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                queue.append((nr, nc))
                arr[nr][nc] = 0


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1

    visited = [[0] * M for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                result += 1
                bfs(i, j)

    print(result)
