# 백준 2444 별 찍기 - 7
# Baekjoon 2444

# Created by sw0817 on 2022. 09. 07..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2444

n = int(input())
t = 1
i = n - 1

for _ in range(2 * n - 1):
    print(' ' * i + '*' * (2 * (n - i) - 1))
    i -= t
    if not i:
        t = -1