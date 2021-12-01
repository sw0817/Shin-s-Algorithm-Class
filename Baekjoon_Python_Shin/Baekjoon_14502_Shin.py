# 백준 14502 욕심쟁이 판다
# Baekjoon 14502

# Created by sw0817 on 2020. 10. 27..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14502


from copy import deepcopy
from collections import deque
from itertools import combinations


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def virus(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        (i, j) = queue.popleft()
        for k in range(4):
            nr = dr[k] + i
            nc = dc[k] + j
            if nr < 0 or nc < 0 or N <= nr or M <= nc:
                continue
            if arr2[nr][nc] == 0:
                arr2[nr][nc] = 2
                queue.append((nr, nc))


N, M = map(int, input().split())
zeros = []
arr = []
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 0:
            zeros.append((i, j))

result = 0
zero_coms = list(combinations(zeros, 3))
for zero_com in zero_coms:
    count = 0
    arr2 = deepcopy(arr)
    for zero in zero_com:
        arr2[zero[0]][zero[1]] = 1
    for i in range(N):
        for j in range(M):
            if arr2[i][j] == 2:
                virus(i, j)
    for i in range(N):
        for j in range(M):
            if arr2[i][j] == 0:
                count += 1
    if count > result:
        result = count

print(result)
