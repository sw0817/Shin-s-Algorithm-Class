# 백준 15666 N과 M (12)
# Baekjoon 15666

# Created by sw0817 on 2021. 05. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15666

from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
repeat = set()
for comb in combinations_with_replacement(nums, M):
    if comb not in repeat:
        repeat.add(comb)
        print(*comb)