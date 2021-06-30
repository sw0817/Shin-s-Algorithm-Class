# 백준 1344 축구
# Baekjoon 1344

# Created by sw0817 on 2021. 06. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1344

import operator
from functools import reduce

# nCr 구하기
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(operator.mul, range(n, n-r, -1), 1)
    denom = reduce(operator.mul, range(1, r+1), 1)
    return numer / denom


# 골 넣을 확률 자체 구하기
def nCr(n, goal):
    return ncr(18, n) * (goal ** n) * ((1-goal) ** (18-n))


# 90분을 5분 간격으로 나누면 18개. 즉 한 팀당 0~18 득점 가능
# 0 ~ 18 중 소수는 2, 3, 5, 7, 11, 13, 17
# 1 - 두 팀 모두 소수가 아닌 숫자로 골을 넣는 확률이 답
nums = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

A = int(input())
B = int(input())
A /= 100
B /= 100

a = b = 0
for num in nums:
    a += nCr(num, A)
    b += nCr(num, B)

print(1-a*b)



