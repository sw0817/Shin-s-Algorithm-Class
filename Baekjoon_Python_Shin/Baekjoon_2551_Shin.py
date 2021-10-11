# 백준 2551 두 대표 자연수
# Baekjoon 2551

# Created by sw0817 on 2021. 10. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2551

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

average = sum(nums) / N
if 0.5 < average - int(average):
    average = int(average) + 1
else:
    average = int(average)
print(nums[(N-1)//2], average)