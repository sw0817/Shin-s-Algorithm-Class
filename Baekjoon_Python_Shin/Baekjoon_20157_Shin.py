# 백준 20157 화살을 쏘자!
# Baekjoon 20157

# Created by sw0817 on 2021. 12. 06..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/20157

from math import gcd

def change(x, y):
    n = gcd(abs(x), abs(y))
    return x // n, y // n


info = dict()
result = 0
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    a, b = change(a, b)
    if (a, b) in info:
        info[(a, b)] += 1
        result = max(result, info[(a, b)])
    else:
        info[(a, b)] = 1
        result = max(result, 1)

print(result)
