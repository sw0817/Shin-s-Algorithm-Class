# 백준 7569 토마토
# Baekjoon 7569

# Created by sw0817 on 2021. 12. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/7569

from collections import deque

dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

M, N, H = map(int, input().split())
cnt = 0
t = -1
queue = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
arr = []
for i in range(H):
    floor = []
    for j in range(N):
        row = list(map(int, input().split()))
        floor.append(row)
        for k in range(M):
            if row[k] == 1:
                visited[i][j][k] = 1
                queue.append((i, j, k))
            elif row[k] == 0:
                cnt += 1
    arr.append(floor)

while queue:
    for _ in range(len(queue)):
        h, r, c = queue.popleft()
        for dh, dr, dc in dir:
            nh, nr, nc = h + dh, r + dr, c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and not visited[nh][nr][nc] and arr[nh][nr][nc] == 0:
                visited[nh][nr][nc] = 1
                queue.append((nh, nr, nc))
                cnt -= 1
    t += 1

print(-1 if cnt else t)