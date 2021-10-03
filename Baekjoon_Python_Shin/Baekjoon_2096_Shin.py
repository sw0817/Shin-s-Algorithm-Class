# 백준 2096 내려가기
# Baekjoon 2096

# Created by sw0817 on 2021. 01. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2096

N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

dp = table[0]
dp2 = table[0]

for i in range(1, N):
    dp = [max(dp[0], dp[1]) + table[i][0], max(dp[0], dp[1], dp[2]) + table[i][1], max(dp[1], dp[2]) + table[i][2]]
    dp2 = [min(dp2[0], dp2[1]) + table[i][0], min(dp2[0], dp2[1], dp2[2]) + table[i][1], min(dp2[1], dp2[2]) + table[i][2]]

print(max(dp), min(dp2))
