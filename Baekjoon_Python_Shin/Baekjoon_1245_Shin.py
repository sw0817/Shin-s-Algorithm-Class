# 백준 1245 농장 관리
# Baekjoon 1245

# Created by sw0817 on 2021. 12. 22..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1245

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

def bfs(r, c, h):
    global result
    plus = 1
    queue = deque()
    queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if h < arr[nr][nc]:
                    plus = 0
                elif h == arr[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
    result += plus


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j, arr[i][j])

print(result)