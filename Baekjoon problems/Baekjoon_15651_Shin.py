# 백준 15651 N과 M (3)
# Baekjoon 15651

# Created by sw0817 on 2021. 05. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15651

from itertools import product

N, M = map(int, input().split())
nums = [i+1 for i in range(N)]
for perm in product(nums, repeat=M):
    print(*perm)