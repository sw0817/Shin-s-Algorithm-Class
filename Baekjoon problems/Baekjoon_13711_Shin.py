# 백준 13711 LCS 4
# Baekjoon 13711

# Created by sw0817 on 2021. 04. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/13711

N = int(input())

str1 = input().replace(' ', '')
str2 = input().replace(' ', '')

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][N])

# 메모리 초과,,