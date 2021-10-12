# 백준 1727 커플 만들기
# Baekjoon 1727

# Created by sw0817 on 2021. 10. 12..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1727

import math

n, m = map(int, input().split())
ns = list(map(int, input().split()))
ms = list(map(int, input().split()))

ns.sort()
ms.sort()

dp = [[math.inf] * m for _ in range(n)]
dp[0][0] = abs(ns[0] - ms[0])
for j in range(1, m):
    dp[0][j] = min(dp[0][j-1], abs(ns[0] - ms[j]))

for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], abs(ns[i] - ms[0]))

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = dp[i-1][j-1] + abs(ns[i] - ms[j])
        if j < i:
            dp[i][j] = min(dp[i][j], dp[i-1][j])
        elif i < j:
            dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[n-1][m-1])