# 백준 1600 말이 되고픈 원숭이
# Baekjoon 1600

# Created by sw0817 on 2021. 07. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1600

from collections import deque

def bfs():
    visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
    queue = deque()
    queue.append((0, 0, K))
    while queue:
        r, c, t = queue.popleft()
        if r == H-1 and c == W-1:
            return visited[r][c][t]
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and not arr[nr][nc] and not visited[nr][nc][t]:
                visited[nr][nc][t] = visited[r][c][t] + 1
                queue.append((nr, nc, t))
        if 0 < t:
            for dr, dc in horse:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and not arr[nr][nc] and not visited[nr][nc][t-1]:
                    visited[nr][nc][t-1] = visited[r][c][t] + 1
                    queue.append((nr, nc, t-1))

    return -1

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
horse = [(2, 1), (1, 2), (-2, 1), (-1, 2), (-1, -2), (-2, -1), (1, -2), (2, -1)]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

print(bfs())