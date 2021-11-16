# 백준 1309 동물원
# Baekjoon 1309

# Created by sw0817 on 2021. 11. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1309

N = int(input())
dp = [1] * (N+2)
for i in range(2, N+2):
    dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

print(dp[N+1])