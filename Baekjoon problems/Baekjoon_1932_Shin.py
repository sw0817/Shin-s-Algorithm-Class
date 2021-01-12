# 백준 1932 정수 삼각형
# Baekjoon 1932

# Created by sw0817 on 2021. 01. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1932

# 삼각형의 크기 n
n = int(input())

# 삼각형 배열
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = []
for i in range(1, n+1):
    dp.append([0] * i)

dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n-1]))

