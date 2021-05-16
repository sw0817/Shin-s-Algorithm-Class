# 백준 15657 N과 M (8)
# Baekjoon 15657

# Created by sw0817 on 2021. 05. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15657

from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for perm in combinations_with_replacement(nums, M):
    print(*perm)