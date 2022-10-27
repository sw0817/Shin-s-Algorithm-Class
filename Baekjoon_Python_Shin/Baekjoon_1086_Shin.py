# 백준 1086 박성원
# Baekjoon 1086

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1086

import math

N = int(input())
nums = [int(input()) for _ in range(N)]
K = int(input())
R = [[(j * 10 ** len(str(nums[i])) + nums[i]) % K for j in range(K)] for i in range(N)]
dp = [[0] * K for _ in range(1 << N)]
dp[0][0] = 1

for b in range(1 << N):
    for i in range(N):
        if b & (1 << i):
            continue
        for j in range(K):
            dp[b | (1 << i)][R[i][j]] += dp[b][j]
p = dp[(1 << N)-1][0]
q = sum(dp[(1 << N) - 1])
g = math.gcd(p, q)
print('{}/{}'.format(p // g, q // g))