# 백준 2225 합분해
# Baekjoon 2225

# Created by sw0817 on 2021. 09. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2225

N, K = map(int, input().split())

memo = [1] * (N + K + 1)

n = 1
for i in range(2, N+K+1):
    n *= i
    memo[i] = n

print(memo[N+K-1] // (memo[K-1] * memo[N]) % 1000000000)