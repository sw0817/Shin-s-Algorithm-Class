# 백준 1003 피보나치 함수
# Baekjoon 1003

# Created by sw0817 on 2021. 07. 05..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1003

T = int(input())
dp = [[0, 0] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1
for i in range(2, 41):
    dp[i][0] = dp[i-2][0] + dp[i-1][0]
    dp[i][1] = dp[i-2][1] + dp[i-1][1]
for _ in range(T):
    N = int(input())
    print(*dp[N])