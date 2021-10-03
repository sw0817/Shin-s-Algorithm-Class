# 백준 1958 LCS 3
# Baekjoon 1958

# Created by sw0817 on 2020. 12. 10..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1958

lst = [input() for i in range(3)]
dp = [[[0 for _ in range(len(lst[0]) + 1)] for j in range(len(lst[1]) + 1)] for k in range(len(lst[2]) + 1)]

for k in range(1, len(lst[2])+1):
    for j in range(1, len(lst[1])+1):
        for i in range(1, len(lst[0])+1):
            if lst[0][i-1] == lst[1][j-1] == lst[2][k-1]:
                dp[k][j][i] = dp[k-1][j-1][i-1] + 1
            else:
                dp[k][j][i] = max(dp[k-1][j][i], dp[k][j-1][i], dp[k][j][i-1], dp[k-1][j-1][i], dp[k][j-1][i-1], dp[k-1][j][i-1])

print(dp[-1][-1][-1])