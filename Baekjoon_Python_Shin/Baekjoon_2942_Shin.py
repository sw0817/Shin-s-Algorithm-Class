# 백준 2942 퍼거슨과 사과
# Baekjoon 2942

# Created by sw0817 on 2022. 01. 07..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2942

from math import gcd

R, G = map(int, input().split())

n = gcd(R, G)
for i in range(1, int(n ** (0.5)) + 1):
    if n / i == n // i:
        print(i, R // i, G // i)
        n_i = n // i
        if i != n_i:
            print(n_i, R // n_i, G // n_i)