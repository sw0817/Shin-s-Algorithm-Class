# 백준 2589 보물섬
# Baekjoon 2589

# Created by sw0817 on 2020. 11. 27..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2589


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    global result
    visited = [[-1] * C for _ in range(R)]
    visited[r][c] = 0
    queue = [(r,c)]
    while queue:
        i, j = queue.pop(0)
        for k in range(4):
            nr = dr[k] + i
            nc = dc[k] + j
            if nr < 0 or nc < 0 or R <= nr or C <= nc or visited[nr][nc] > -1 or arr[nr][nc] == 'W':
                continue
            visited[nr][nc] = visited[i][j] + 1
            queue.append((nr, nc))
            if visited[nr][nc] > result:
                result = visited[nr][nc]



R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
result = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            bfs(i, j)

print(result)
