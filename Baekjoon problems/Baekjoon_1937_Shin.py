# 백준 1937 욕심쟁이 판다
# Baekjoon 1937

# Created by sw0817 on 2020. 10. 24..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1937


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def panda(i, j):
    if visited[i][j] < 0:
        visited[i][j] = 0

        for k in range(4):
            nr = dr[k] + i
            nc = dc[k] + j
            if nr < 0 or nc < 0 or N <= nr or N <= nc:
                continue
            else:
                if arr[i][j] < arr[nr][nc]:
                    visited[i][j] = max(visited[i][j], panda(nr, nc))
        visited[i][j] += 1
    return visited[i][j]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        result = max(result, panda(i, j))

print(result)

