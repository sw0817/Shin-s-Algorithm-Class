# 백준 17836 공주님을 구해라!
# Baekjoon 17836

# Created by sw0817 on 2021. 12. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17836

import math
from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M, T = map(int, input().split())
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 2:
            gram = (i, j)
visited = [[math.inf] * M for _ in range(N)]
visited[0][0] = 0
queue = deque()
queue.append((0, 0))
t = 0
while queue:
    t += 1
    if t == T+1:
        break
    for _ in range(len(queue)):
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and t < visited[nr][nc] and arr[nr][nc] != 1:
                visited[nr][nc] = t
                queue.append((nr, nc))

r, c = gram
result = min(visited[N-1][M-1], visited[r][c] + (M-1-c) + (N-1-r))
print('Fail' if T < result else result)