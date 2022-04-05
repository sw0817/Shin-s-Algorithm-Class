# 백준 2003 수들의 합 2
# Baekjoon 2003

# Created by sw0817 on 2022. 04. 05..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

l = 0
r = 1
cur = nums[0]

if cur == M:
    result += 1

while True:
    if l == r == N:
        break
    if cur < M and r < N:
        cur += nums[r]
        r += 1
    else:
        cur -= nums[l]
        l += 1
    if cur == M:
        result += 1

print(result)