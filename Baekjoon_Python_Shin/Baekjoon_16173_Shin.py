# 백준 16173 점프왕 쩰리 (Small)
# Baekjoon 16173

# Created by sw0817 on 2022. 09. 28..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/16173

from collections import deque

move = [(1, 0), (0, 1)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
result = 'Hing'
while queue:
    r, c = queue.popleft()
    if r == N-1 and c == N-1:
        result = 'HaruHaru'
        break
    n = arr[r][c]
    for dr, dc in move:
        nr, nc = r + dr * n, c + dc * n
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = 1
            queue.append((nr, nc))

print(result)