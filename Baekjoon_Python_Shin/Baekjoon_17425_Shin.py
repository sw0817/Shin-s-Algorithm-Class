# 백준 17425 약수의 합
# Baekjoon 17425

# Created by sw0817 on 2021. 12. 05..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17425

from sys import stdin

divisors = [1] * 1000001

for i in range(2, 1000001):
    for j in range(i, 1000001, i):
        divisors[j] += i
    divisors[i] += divisors[i-1]

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    print(divisors[N])