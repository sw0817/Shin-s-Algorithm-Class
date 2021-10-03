# 백준 15654 N과 M (5)
# Baekjoon 15654

# Created by sw0817 on 2021. 05. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15654

from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for perm in permutations(nums, M):
    print(*perm)