# 백준 2749 피보나치 수 3
# Baekjoon 2749

# Created by sw0817 on 2022. 10. 19..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2749

n = int(input())
a, b, c = 0, 1, 10 ** 5
n = n % (c * 15)
c *= 10

for i in range(n):
    a, b = b % c, (a + b) % c

print(a)