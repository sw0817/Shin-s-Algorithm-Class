# 백준 2750 수 정렬하기
# Baekjoon 2750

# Created by sw0817 on 2022. 11. 24..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2750

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
for i in range(N):
    print(nums[i])