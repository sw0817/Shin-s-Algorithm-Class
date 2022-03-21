# 백준 17298 오큰수
# Baekjoon 17298

# Created by sw0817 on 2022. 03. 21..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17298

N = int(input())
nums = list(map(int, input().split()))
result = [-1] * N

stack = [0]
for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)