# 백준 1695 팰린드롬 만들기
# Baekjoon 1695

# Created by sw0817 on 2021. 03. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1695

N = int(input())
array = list(map(int, input().split()))
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if array[i-1] == array[N-j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(N - dp[N][N])
