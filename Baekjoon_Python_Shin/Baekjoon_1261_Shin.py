# 백준 1261 알고스팟
# Baekjoon 1261

# Created by sw0817 on 2022. 10. 30..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1261

from collections import deque

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

queue = deque()
queue.append((0, 0))
dist[0][0] = 0

while queue:
    r, c = queue.popleft()
    for dr, dc in move:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if dist[nr][nc] == -1:
                if arr[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c]
                    queue.appendleft((nr, nc))
                else:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

print(dist[N-1][M-1])