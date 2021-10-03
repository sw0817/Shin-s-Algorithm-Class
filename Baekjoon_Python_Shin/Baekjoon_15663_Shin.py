# 백준 15663 N과 M (9)
# Baekjoon 15663

# Created by sw0817 on 2021. 05. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15663

from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
repeat = set()
for perm in permutations(nums, M):
    if perm not in repeat:
        repeat.add(perm)
        print(*perm)