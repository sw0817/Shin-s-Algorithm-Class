# 백준 1011 Fly me to the Alpha Centauri
# Baekjoon 1011

# Created by sw0817 on 2021. 11. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1011

import math

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x
    i = math.floor(d ** 0.5)
    l = i * 2 - 1
    r = d - i ** 2
    if r:
        l += 1
        if i < r:
            l += 1
    print(l)