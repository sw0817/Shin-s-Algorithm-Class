# 백준 1509 팰린드롬 분할
# Baekjoon 1509

# Created by sw0817 on 2021. 01. 31..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1509

s = input()
l = len(s)

dp = [[0 for _ in range(l+1)] for _ in range(l+1)]
result = [l+2] * (l+1)
result[0] = 0

for i in range(1, l+1):
    dp[i][i] = 1

for i in range(1, l):
    if s[i-1] == s[i]:
        dp[i][i+1] = 1

for i in range(2, l):
    for j in range(1, l+1-i):
        if s[j-1] == s[j+1-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(1, l+1):
    result[i] = min(result[i], result[i-1]+1)
    for j in range(i+1, l+1):
        if dp[i][j] != 0:
            result[j] = min(result[j], result[i-1]+1)

print(result[l])

# 틀렸어요.