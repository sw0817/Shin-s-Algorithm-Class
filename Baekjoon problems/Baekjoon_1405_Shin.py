# 백준 1405 미친 로봇
# Baekjoon 1405

# Created by sw0817 on 2021. 09. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1405

from collections import deque

def recur(i, j, n, p):
    global result
    if n == N:
        return
    for dr, dc, t_p in move:
        nr, nc = i + dr, j + dc
        if visited[nr][nc]:
            result -= p * t_p / 100
        else:
            visited[nr][nc] = 1
            recur(nr, nc, n+1, p * t_p / 100)
            visited[nr][nc] = 0


result = 1
N, east, west, south, north = map(int, input().split())
move = [(0, 1, east),(0, -1, west), (1, 0, south), (-1, 0, north)]
queue = deque()
visited = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
visited[N][N] = 1
for dr, dc, p in move:
    nr, nc = N + dr, N + dc
    visited[nr][nc] = 1
    recur(nr, nc, 1, p / 100)
    visited[nr][nc] = 0

print(result)
