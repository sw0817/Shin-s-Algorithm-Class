# 백준 4307 개미
# Baekjoon 4307

# Created by sw0817 on 2022. 01. 23..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4307

T = int(input())
for _ in range(T):
    l, n = map(int, input().split())
    min_, max_ = 0, 0
    for _ in range(n):
        p = int(input())
        min_ = max(min_, min(p, l - p))
        max_ = max(max_, p, l - p)

    print(min_, max_)