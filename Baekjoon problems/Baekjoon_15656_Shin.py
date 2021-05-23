# 백준 15656 N과 M (7)
# Baekjoon 15656

# Created by sw0817 on 2021. 05. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15656

from itertools import product

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for perm in product(nums, repeat=M):
    print(*perm)