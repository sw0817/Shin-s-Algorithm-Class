# 백준 2118 두 개의 탑
# Baekjoon 2118

# Created by sw0817 on 2022. 01. 06..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2118

N = int(input())
nums = []
acc = 0
result = 0

for _ in range(N):
    num = int(input())
    nums.append(num)
    acc += num
nums.append(0)

l, r = 0, 0
cur = nums[0]

while l <= r and r < N:
    short = min(cur, acc-cur)
    result = max(result, short)
    if short == cur:
        r += 1
        cur += nums[r]
    else:
        cur -= nums[l]
        l += 1

print(result)