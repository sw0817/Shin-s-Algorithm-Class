# 백준 15650 N과 M (2)
# Baekjoon 15650

# Created by sw0817 on 2021. 05. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15650

from itertools import combinations

N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
for comb in combinations(nums, M):
    print(*comb)