# 백준 2023 신기한 소수
# Baekjoon 2023

# Created by sw0817 on 2021. 08. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2023

# 8자리는 10,000,000

n = 10000000
a = [True] * n
primes = set()
for i in range(2, int(n ** 0.5) + 1):
    if a[i]:
        primes.add(i)
        for j in range(2*i, n, i):
            a[j] = False

N = int(input())
for prime in primes:
    if 10 ** (N-1) <= prime < 10 ** N:
        check = True
        p = str(prime)
        for j in range(1, len(p)-1):
            if not int(p[:j]) in primes:
                check = False
                break
        if check:
            print(p)

# 메모리 초과