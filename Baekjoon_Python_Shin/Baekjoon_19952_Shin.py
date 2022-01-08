# 백준 19952 인성 문제 있어??
# Baekjoon 19952

# Created by sw0817 on 2022. 01. 08..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/19952

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for _ in range(T):
    H, W, O, F, Sx, Sy, Ex, Ey = map(int, input().split())
    arr = [[0] * W for _ in range(H)]
    visited = [[-1] * W for _ in range(H)]
    for _ in range(O):
        X, Y, L = map(int, input().split())
        arr[X-1][Y-1] = L
    can = False
    queue = deque()
    queue.append((Sx-1, Sy-1))
    visited[Sx-1][Sy-1] = F
    while queue:
        if can:
            break
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) == (Ex-1, Ey-1):
                can = True
                break
            if not F:
                continue
            h = arr[r][c]
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and visited[nr][nc] < F-1 and arr[nr][nc] <= F + h:
                    visited[nr][nc] = F-1
                    queue.append((nr, nc))
        F -= 1

    if can or (Ex, Ey) == (Sx, Sy):
        print('잘했어!!')
    else:
        print('인성 문제있어??')