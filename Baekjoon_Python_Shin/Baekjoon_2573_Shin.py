# 백준 5427 불
# Baekjoon 5427

# Created by sw0817 on 2021. 12. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5427

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(r, c):
    t = 1
    queue = deque()
    queue.append((r, c))
    while queue:
        for _ in range(len(fire)):
            r, c = fire.popleft()
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] in ['.', '@']:
                    arr[nr][nc] = '*'
                    fire.append((nr, nc))

        for _ in range(len(queue)):
            r, c = queue.popleft()
            if r == 0 or r == h-1 or c == 0 or c == w-1:
                return t
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and arr[nr][nc] == '.':
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

        t += 1


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = []
    cnt = 0
    fire = deque()
    for i in range(h):
        row = list(input())
        arr.append(row)
        for j in range(w):
            if row[j] == '*':
                fire.append((i, j))
            elif row[j] == '@':
                start = (i, j)

    visited = [[0] * w for _ in range(h)]
    i, j = start
    visited[i][j] = 1
    t = bfs(i, j)
    print(t if t else 'IMPOSSIBLE')
