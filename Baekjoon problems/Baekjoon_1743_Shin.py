# 백준 1743 음식물 피하기
# Baekjoon 1743

# Created by sw0817 on 2021. 02. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1743

# 간단한 BFS문제

from _collections import deque


next = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M, K = map(int, input().split())

dust = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    dust[r-1][c-1] = 1

result = 0

for i in range(N):
    for j in range(M):
        if dust[i][j]:
            cnt = 0
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                r, c = queue.popleft()
                for dr, dc in next:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and dust[nr][nc]:
                        dust[nr][nc] = 0
                        queue.appendleft((nr, nc))
                        cnt += 1

            if result < cnt:
                result = cnt

print(result)