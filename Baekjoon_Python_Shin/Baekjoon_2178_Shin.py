# 백준 2178 미로 탐색
# Baekjoon 2178

# Created by sw0817 on 2021. 11. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2178

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
queue = deque()
queue.append((0, 0))
result = 0
while queue:
    result += 1
    for _ in range(len(queue)):
        r, c = queue.popleft()
        if r == N-1 and c == M-1:
            queue.clear()
            break
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == '1':
                visited[nr][nc] = 1
                queue.append((nr, nc))

print(result)