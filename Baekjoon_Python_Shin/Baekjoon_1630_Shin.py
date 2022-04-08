# 백준 1630 오민식
# Baekjoon 1630

# Created by sw0817 on 2022. 04. 08..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1630

N = int(input())
mod = 987654321
prime = [False] * (N + 1)
result = 1
for i in range(2, N+1):
    if not prime[i]:
        n = i * 2
        while n <= N:
            prime[n] = True
            n += i
        n = i
        while n <= N:
            n *= i
        result = (result * (n // i)) % mod

print(result)