# 백준 1725 히스토그램
# Baekjoon 1725

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1725

N = int(input())

histogram = []

result = 0
idx = 0

for _ in range(N):
    histogram.append(int(input()))
histogram.append(0)

stack = [(0, histogram[0])]
for i in range(1, N+1):
    idx = i
    while stack and stack[-1][1] > histogram[i]:
        idx, temp = stack.pop()
        result = max(result, temp*(i-idx))
    stack.append((idx, histogram[i]))

print(result)