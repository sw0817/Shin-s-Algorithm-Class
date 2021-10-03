# 백준 1074 Z
# Baekjoon 1074

# Created by sw0817 on 2021. 03. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1074

n, r, c = map(int, input().split())
num = 0

while n > 0:
    temp = (2 ** n) // 2
    if n > 1:
        if temp > r and temp <= c:
            num += temp ** 2
            c -= temp
        elif temp <= r and temp > c:
            num += (temp ** 2) * 2
            r -= temp
        elif temp <= r and temp <= c:
            num += (temp ** 2) * 3
            r -= temp
            c -= temp

    elif n == 1:
        if r == 0 and c == 1:
            num += 1
        elif r == 1 and c == 0:
            num += 2
        elif r == 1 and c == 1:
            num += 3
    n -= 1

print(num)

