# 백준 12013 248 게임
# Baekjoon 12013

# Created by sw0817 on 2021. 04. 18..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/12013

N = int(input())
arr = []
dp = [[0] * N for _ in range(N)]
result = 0

for i in range(N):
    num = int(input())
    arr.append(num)
    dp[i][i] = num
    result = max(result, num)

for s in range(1, N+1):
    for i in range(N-s):
        num = i + s
        for j in range(i, num):
            if dp[i][j] == dp[j+1][num] and dp[i][j] != 0:
                dp[i][num] = max(dp[i][num], dp[i][j] + 1)
            result = max(result, dp[i][num])

print(result)