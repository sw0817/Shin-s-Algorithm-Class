# 백준 6549 히스토그램에서 가장 큰 직사각형
# Baekjoon 6549

# Created by sw0817 on 2021. 03. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/6549

while True:
    info = list(map(int, input().split()))
    N = info[0]
    if N == 0:
        break

    result = 0
    histogram = info[1:]
    histogram.append(0)
    stack = [(0, histogram[0])]
    for i in range(1, N+1):
        idx = i
        while stack and stack[-1][1] > histogram[i]:
            idx, temp = stack.pop()
            result = max(result, temp*(i-idx))
        stack.append((idx, histogram[i]))

    print(result)