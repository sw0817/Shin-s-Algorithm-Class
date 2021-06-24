# 백준 1937 욕심쟁이 판다
# Baekjoon 1937

# Created by sw0817 on 2020. 12. 01..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1937


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs1(i, j):
    queue = [(i, j)]
    while queue:
        i, j = queue.pop(0)
        arr[i][j] = a
        for k in range(4):
            nr = dr[k] + i
            nc = dc[k] + j
            print((nr, nc))
            if nr < 0 or nc < 0 or N <= nr or N <= nc:
                continue
            if arr[nr][nc] == 1:
                queue.append((nr, nc))


N = int(input())
arr = [list(map(int, input().split()))]
visited = [[0] * N for _ in range(N)]
a = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs1(i, j)
            a += 1

print(arr)