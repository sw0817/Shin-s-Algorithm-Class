# 백준 1941 소문난 칠공주
# Baekjoon 1941

# Created by sw0817 on 2022. 04. 19..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1941

from collections import deque
from itertools import combinations

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

result = 0
arr = []
comb_list = []
for i in range(5):
    arr.append(input())
    for j, n in enumerate(arr[i]):
        comb_list.append((i, j))

for comb in combinations(comb_list, 7):
    comb = list(comb)
    r, c = comb[0]
    n = arr[r][c]
    y = s = 0
    cnt = 1
    if n == 'Y':
        y += 1
    else:
        s += 1
    queue = deque()
    queue.append((r, c))
    comb.remove((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nr < 5 and (nr, nc) in comb:
                queue.append((nr, nc))
                comb.remove((nr, nc))
                cnt += 1
                if arr[nr][nc] == 'Y':
                    y += 1
                else:
                    s += 1
    if cnt == 7 and y < 4:
        result += 1

print(result)