# 백준 1687 행렬 찾기
# Baekjoon 1687

# Created by sw0817 on 2022. 10. 10..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1687

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
h_arr = [[0] * (M+1) for _ in range(N)]

for j in range(M):
    if arr[0][j] == '0':
        h_arr[0][j] = 1

for i in range(1, N):
    for j in range(M):
        if arr[i][j] == '0':
            h_arr[i][j] = h_arr[i-1][j] + 1

result = 0
for i in range(N):
    stack = [(0, h_arr[i][0])]
    for j in range(1, M+1):
        idx = j
        while stack and h_arr[i][j] < stack[-1][1]:
            idx, tmp = stack.pop()
            result = max(result, tmp * (j - idx))
        stack.append((idx, h_arr[i][j]))

print(result)