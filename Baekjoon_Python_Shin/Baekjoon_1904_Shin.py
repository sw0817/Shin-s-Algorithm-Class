# 백준 1904 01타일
# Baekjoon 1904

# Created by sw0817 on 2022. 03. 24..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1904

N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    a, b, c = 1, 2, 3
    for i in range(3, N+1):
        c = (a + b) % 15746
        a, b = b, c
    print(c)