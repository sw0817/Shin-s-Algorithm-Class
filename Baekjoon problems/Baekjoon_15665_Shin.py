# 백준 15665 N과 M (11)
# Baekjoon 15665

# Created by sw0817 on 2021. 05. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15665

from itertools import product

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
repeat = set()
for perm in product(nums, repeat=M):
    if perm not in repeat:
        repeat.add(perm)
        print(*perm)