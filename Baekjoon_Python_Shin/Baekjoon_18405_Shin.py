# 백준 18405 경쟁적 전염
# Baekjoon 18405

# Created by sw0817 on 2022. 04. 27..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/18405

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, K = map(int, input().split())

arr = []
virus = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            virus.append((row[j], i, j))
    arr.append(row)

virus.sort()
curVirus = deque()
for vir in virus:
    curVirus.append(vir)

S, X, Y = map(int, input().split())
for _ in range(S):
    nxtVirus = deque()
    while curVirus:
        n, r, c = curVirus.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc]:
                arr[nr][nc] = n
                nxtVirus.append((n, nr, nc))
    curVirus = nxtVirus

print(arr[X-1][Y-1])