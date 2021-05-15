# 백준 15649 N과 M (1)
# Baekjoon 15649

# Created by sw0817 on 2021. 05. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15649

from itertools import permutations

N, M = map(int, input().split())
nums = [i+1 for i in range(N)]
for perm in permutations(nums, M):
    print(*perm)