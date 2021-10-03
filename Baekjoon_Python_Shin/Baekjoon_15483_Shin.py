# 백준 15483 최소 편집
# Baekjoon 15483

# Created by sw0817 on 2021. 04. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15483

str1 = input()
str2 = input()
l1 = len(str1)
l2 = len(str2)

dp = [[0] * (l2+1) for _ in range(l1+1)]

for i in range(l1+1):
    dp[i][0] = i

for i in range(l2+1):
    dp[0][i] = i

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1

print(dp[l1][l2])