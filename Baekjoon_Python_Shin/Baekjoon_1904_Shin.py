# 백준 1904 01타일
# Baekjoon 1904

# Created by sw0817 on 2022. 03. 24..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1904

N = int(input())
if N == 1:
    print(1)
else:
    dp = [0] * (N+1)
    dp[1], dp[2] = 1, 2
    if 2 < N:
        for i in range(3, N+1):
            dp[i] = (dp[i-2] + dp[i-1]) % 15746

    print(dp[N])
