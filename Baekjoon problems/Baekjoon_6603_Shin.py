# 백준 6603 로또
# Baekjoon 6603

# Created by sw0817 on 2021. 01. 23..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/6603

from itertools import combinations


while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    nums.pop(0)
    coms = list(combinations(nums, 6))
    for com in coms:
        print(*com)
    print()