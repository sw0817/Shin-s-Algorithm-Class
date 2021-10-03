# 백준 1565 수학
# Baekjoon 1565

# Created by sw0817 on 2021. 08. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1565

from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)


def getMDivisor(d):
    divisor = []
    for i in range(1, int(d ** 0.5) + 1):
        if not d % i:
            if min_num <= i:
                divisor.append(i)
            if i ** 2 != d:
                if min_num <= d // i:
                    divisor.append(d // i)
    divisor.sort()
    return divisor


def check(n):
    for i in range(1, len_M):
        if M[i] % n:
            return False
    return True


len_D, len_M = map(int, input().split())
D = list(map(int, input().split()))
M = list(map(int, input().split()))

min_num = 1
for i in range(len_D):
    min_num = lcm(min_num, D[i])

result = 0
M.sort()
min_divisor = getMDivisor(M[0])
for divisor in min_divisor:
    if not divisor % min_num:
        if check(divisor):
            result += 1

print(result)