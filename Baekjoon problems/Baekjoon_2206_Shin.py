# 백준 2206 벽 부수고 이동하기
# Baekjoon 2206

# Created by sw0817 on 2021. 01. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2206

from _collections import deque


next = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0][1] = 1
    while queue:
        r, c, w = queue.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c][w]
        for dr, dc in next:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and w == 1:
                    visited[nr][nc][0] = visited[r][c][1] + 1
                    queue.append((nr, nc, 0))
                elif arr[nr][nc] == 0 and visited[nr][nc][w] == 0:
                    visited[nr][nc][w] = visited[r][c][w] + 1
                    queue.append((nr, nc, w))

    return -1


N, M = map(int, input().split())
arr = []

for i in range(N):
    row = list(map(int, input()))
    arr.append(row)

print(bfs())