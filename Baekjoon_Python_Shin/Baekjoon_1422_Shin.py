# 백준 1422 숫자의 신
# Baekjoon 1422

# Created by sw0817 on 2021. 03. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1422

from functools import cmp_to_key

K, N = map(int, input().split())

nums = [int(input()) for _ in range(K)]
max_n = max(nums)

for _ in range(N - len(nums)):
    nums.append(max_n)

nums = sorted(nums, key=cmp_to_key(lambda a, b: -1 if int(str(a)+str(b)) > int(str(b)+str(a)) else 1))
print(*nums, sep='')