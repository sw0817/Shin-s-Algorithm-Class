# 백준 15655 N과 M (6)
# Baekjoon 15655

# Created by sw0817 on 2021. 05. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15655

from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for perm in combinations(nums, M):
    print(*perm)