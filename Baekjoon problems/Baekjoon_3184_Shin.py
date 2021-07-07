# 백준 3184 양
# Baekjoon 3184

# Created by sw0817 on 2021. 07. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3184

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
sheep = 0
wolf = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'o' and not visited[i][j] or arr[i][j] == 'v' and not visited[i][j]:
            s, w = 0, 0
            if arr[i][j] == 'o':
                s += 1
            else:
                w += 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and not arr[nr][nc] == '#':
                        if arr[nr][nc] == 'o':
                            s += 1
                        elif arr[nr][nc] == 'v':
                            w += 1
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
            if w < s:
                sheep += s
            else:
                wolf += w

print(sheep, wolf)