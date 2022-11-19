# 백준 2156 포도주 시식
# Baekjoon 2156

# Created by sw0817 on 2022. 11. 19..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2156

def solve():
    n = int(input())
    g = []
    for _ in range(n):
        g.append(int(input()))

    if n < 3:
        return sum(g)

    dp = [0] * (n+1)
    dp[1] = g[0]
    dp[2] = g[0] + g[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i-1], dp[i-3] + g[i-2] + g[i-1], dp[i-2] + g[i-1])

    return dp[n]


print(solve())
