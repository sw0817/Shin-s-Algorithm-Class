# 백준 1463 1로 만들기
# Baekjoon 1463

# Created by sw0817 on 2022. 10. 09..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1463

N = int(input())
dp = [0] * (N)
for i in range(1, N):
    if not (i+1) % 3:
        dp[i] = min(dp[(i+1) // 3 - 1], dp[i-1]) + 1
    elif not (i+1) % 2:
        dp[i] = min(dp[(i+1) // 2 - 1], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[N-1])