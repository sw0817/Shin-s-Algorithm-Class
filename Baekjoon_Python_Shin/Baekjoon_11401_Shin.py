# 백준 11401 이항 계수 3
# Baekjoon 11401

# Created by sw0817 on 2022. 10. 26..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11401

def factorial(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % p
    return n


def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p


N, K = map(int, input().split())
p = 1000000007

top = factorial(N)
bot = factorial(N - K) * factorial(K) % p

print(top * square(bot, p - 2) % p)