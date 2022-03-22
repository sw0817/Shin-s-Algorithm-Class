# 백준 12865 평범한 배낭
# Baekjoon 12865

# Created by sw0817 on 2022. 03. 22..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]

bag = []
for _ in range(N):
    bag.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    w, v = bag[i-1]
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])
