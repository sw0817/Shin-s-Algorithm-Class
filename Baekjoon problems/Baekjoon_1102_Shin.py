# 백준 1328 고층 빌딩
# Baekjoon 1328

# Created by sw0817 on 2021. 04. 03..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1328

N, L, R = map(int, input().split())
dp = [[[0] * (R+1) for _ in range(L+1)] for _ in range(N+1)]
dp[1][1][1] = 1

for i in range(2, N+1):
    for j in range(1, L+1):
        for k in range(1, R+1):
            dp[i][j][k] = (dp[i-1][j][k] * (i-2) % 1000000007 + dp[i-1][j][k-1] % 1000000007 + dp[i-1][j-1][k] % 1000000007)

print(dp[N][L][R] % 1000000007)