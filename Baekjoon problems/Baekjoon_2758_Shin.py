# 백준 2758 로또
# Baekjoon 2758

# Created by sw0817 on 2021. 03. 01..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2758

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    dp = [[-1] * (m+1) for _ in range(n)]
    for i in range(m+1):
        dp[0][i] = i

    for i in range(1, n):
        dp[i][0] = 0

    for i in range(1, n):
        for j in range(2 ** i):
            if m < j:
                break
            dp[i][j] = 0
        for j in range(2 ** i, m+1):
            if m // (2 ** (n-i-1)) < j:
                continue
            dp[i][j] = dp[i-1][j//2] + dp[i][j-1]

    print(dp[n-1][m])