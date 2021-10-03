# 백준 2718 타일 채우기
# Baekjoon 2718

# Created by sw0817 on 2021. 04. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2718

T = int(input())

dp = [[0] * 16 for _ in range(10001)]
dp[0][15] = 1
for i in range(1, 10001):
    for j in range(16):
        dp[i][j] = dp[i-1][15-j]
    dp[i][3] += dp[i-1][15]
    dp[i][6] += dp[i-1][15]
    dp[i][7] += (dp[i-1][14] + dp[i-1][11])
    dp[i][11] += dp[i-1][7]
    dp[i][12] += dp[i-1][15]
    dp[i][13] += dp[i-1][14]
    dp[i][14] += (dp[i-1][7] + dp[i-1][13])
    dp[i][15] += (dp[i-1][15] + dp[i-1][3] + dp[i-1][12] + dp[i-1][6])

for tc in range(1, T+1):
    n = int(input())
    print(dp[n][15])