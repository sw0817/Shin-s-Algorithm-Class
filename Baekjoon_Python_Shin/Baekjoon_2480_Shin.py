# 백준 2480 주사위 세개
# Baekjoon 2480

# Created by sw0817 on 2021. 09. 01..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2480

a, b, c = map(int, input().split())
nums = [0] * 7
nums[a] += 1
nums[b] += 1
nums[c] += 1

result = 0
if max(nums) == 1:
    for i in range(7):
        if nums[i]:
            result = i * 100
    print(result)
else:
    for i in range(7):
        if nums[i] == 3:
            print(10000 + i * 1000)
        elif nums[i] == 2:
            print(1000 + i * 100)