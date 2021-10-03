# 백준 15664 N과 M (10)
# Baekjoon 15664

# Created by sw0817 on 2021. 05. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15664

from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
repeat = set()
for comb in combinations(nums, M):
    if comb not in repeat:
        repeat.add(comb)
        print(*comb)