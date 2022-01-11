# 백준 16973 직사각형 탈출
# Baekjoon 16973

# Created by sw0817 on 2022. 01. 11..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/16973

from collections import deque

def bfs():
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) == (Fr - 1, Fc - 1):
                return cnt
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N - H + 1 and 0 <= nc < M - W + 1 and not visited[nr][nc] and not arr[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
        cnt += 1
    return -1


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
arr = [[0] * (M+1) for _ in range(N+1)]
wall = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j]:
            wall.append((i, j))

H, W, Sr, Sc, Fr, Fc = map(int, input().split())
for i, j in wall:
    r, c = max(0, i-H+1), max(0, j-W+1)
    arr[r][c] += 1
    arr[i+1][c] -= 1
    arr[r][j+1] -= 1
    arr[i+1][j+1] += 1

for i in range(N):
    for j in range(1, M+1):
        arr[i][j] += arr[i][j-1]

for j in range(M):
    for i in range(1, N+1):
        arr[i][j] += arr[i-1][j]

result = 0
visited = [[0] * M for _ in range(N)]
queue = deque()
visited[Sr-1][Sc-1] = 1
queue.append((Sr-1, Sc-1))
print(bfs())