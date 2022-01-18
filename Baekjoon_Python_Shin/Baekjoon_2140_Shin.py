# 백준 2140 지뢰찾기
# Baekjoon 2140

# Created by sw0817 on 2022. 01. 18..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2140

delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
nums = list(i for i in range(10))

N = int(input())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    arr[0][i] = int(arr[0][i])
    arr[N-1][i] = int(arr[N-1][i])

for i in range(1, N-1):
    arr[i][0] = int(arr[i][0])
    arr[i][-1] = int(arr[i][-1])

result = 0
for i in range(1, N-1):
    for j in range(1, N-1):
        if 1 < i and i < N-2 and 1 < j and j < N-2:
            result += 1
            continue
        pos = True
        for dr, dc in delta:
            nr, nc = i + dr, j + dc
            if arr[nr][nc] in nums:
                if arr[nr][nc] == 0:
                    pos = False
                    break
        if pos:
            for dr, dc in delta:
                nr, nc = i + dr, j + dc
                if arr[nr][nc] in nums:
                    arr[nr][nc] -= 1
            result += 1

print(result)