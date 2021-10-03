# 백준 1292 쉽게 푸는 문제
# Baekjoon 1292

# Created by sw0817 on 2021. 08. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1292

nums = []
for i in range(1, 46):
    nums.extend([i] * i)

A, B = map(int, input().split())
print(sum(nums[A-1:B]))