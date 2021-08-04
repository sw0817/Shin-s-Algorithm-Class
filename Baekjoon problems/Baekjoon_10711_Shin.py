# 백준 10711 모래성
# Baekjoon 10711

# Created by sw0817 on 2021. 08. 04..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10711

from collections import deque

def check(R, C):
    for dr, dc in eight:
        nr, nc = R + dr, C + dc
        if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] != '.':
            arr[nr][nc] -= 1
            if arr[nr][nc] == 0:
                arr[nr][nc] = '.'
                queue.append((nr, nc))


eight = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

H, W = map(int, input().split())
arr = []
queue = deque()
for i in range(H):
    row = list(input())
    for j in range(W):
        if row[j].isdigit():
            row[j] = int(row[j])
        else:
            queue.append((i, j))
    arr.append(row)

result = -1
while queue:
    result += 1
    for _ in range(len(queue)):
        r, c = queue.popleft()
        check(r, c)

print(result)