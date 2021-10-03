# 백준 1303 전쟁 - 전투
# Baekjoon 1303

# Created by sw0817 on 2021. 02. 22..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1303

from collections import deque

next = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())

war = [list(input()) for _ in range(M)]

W = 0
B = 0

for i in range(M):
    for j in range(N):
        if war[i][j] == 'W':
            war[i][j] = 0
            cnt = 1
            queue = deque()
            queue.append((i, j))
            while queue:
                r, c = queue.pop()
                for dr, dc in next:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < M and 0 <= nc < N and war[nr][nc] == 'W':
                        war[nr][nc] = 0
                        cnt += 1
                        queue.append((nr, nc))
            W += cnt ** 2

        elif war[i][j] == 'B':
            war[i][j] = 0
            cnt = 1
            queue = deque()
            queue.append((i, j))
            while queue:
                r, c = queue.pop()
                for dr, dc in next:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < M and 0 <= nc < N and war[nr][nc] == 'B':
                        war[nr][nc] = 0
                        cnt += 1
                        queue.append((nr, nc))
            B += cnt ** 2

print('{} {}'.format(W, B))