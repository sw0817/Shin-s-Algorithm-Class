# 백준 1562 계단 수
# Baekjoon 1562

# Created by sw0817 on 2021. 07. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1562

N = int(input())

dp = [[0] * 1024 for _ in range(10)]

for i in range(1, 10):
    dp[i][2 ** i] = 1

for i in range(1, N):
    n_dp = [[0] * 1024 for _ in range(10)]
    for r in range(10):
        for c in range(1024):
            if r < 9:
                n_dp[r][c | (1 << r)] = (n_dp[r][c | (1 << r)] + dp[r+1][c]) % 1000000000
            if r > 0:
                n_dp[r][c | (1 << r)] = (n_dp[r][c | (1 << r)] + dp[r-1][c]) % 1000000000
    dp = n_dp

print(sum([dp[i][1023] for i in range(10)]) % 1000000000)