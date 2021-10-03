# 백준 1546 평균
# Baekjoon 1546

# Created by sw0817 on 2021. 06. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1546

N = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
max_num = nums[0]
result = 0
for i in range(N):
    result += nums[i]*100/max_num

result /= N
print(result)