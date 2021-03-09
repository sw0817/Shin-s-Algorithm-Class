# 백준 10026 적록색약
# Baekjoon 10026

# Created by sw0817 on 2021. 03. 09..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10026

from _collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
result = result2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            C = arr[i][j]
            while queue:
                r, c = queue.popleft()
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] == C:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
            result += 1

        if not visited2[i][j]:
            queue = deque()
            queue.append((i, j))
            if arr[i][j] == 'B':
                C = 'B'
            else:
                C = 'RG'
            visited2[i][j] = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not visited2[nr][nc]:
                        if C == 'B' and arr[nr][nc] == 'B' or C == 'RG' and arr[nr][nc] == 'R' or C == 'RG' and arr[nr][nc] == 'G':
                            visited2[nr][nc] = 1
                            queue.append((nr, nc))
            result2 += 1

print("{} {}".format(result, result2))