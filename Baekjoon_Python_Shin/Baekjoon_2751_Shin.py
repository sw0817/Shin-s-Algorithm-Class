# 백준 2751 수 정렬하기 2
# Baekjoon 2751

# Created by sw0817 on 2022. 10. 03..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2751

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort()
for i in range(N):
    print(nums[i])