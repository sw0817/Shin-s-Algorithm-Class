# 백준 2981 검문
# Baekjoon 2981

# Created by sw0817 on 2021. 12. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2981

import sys
from math import gcd

N = int(input())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
nums.sort(reverse=True)
gcd_list = []

for i in range(len(nums) - 1):
    gcd_list.append(nums[i] - nums[i + 1])

n = gcd_list[0]
for i in range(1, len(gcd_list)):
    n = gcd(n, gcd_list[i])

result = set()
for i in range(2, int(n ** 0.5) + 1):
    if not n % i:
        result.add(i)
        result.add(n // i)

result.add(n)
result = list(result)
result.sort()
print(*result)