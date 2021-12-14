# 백준 11049 행렬 곱셈 순서
# Baekjoon 11049

# Created by sw0817 on 2021. 12. 14..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11049

import math

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(N-i):
        k = i + j
        dp[j][k] = math.inf
        for o in range(j, k):
            dp[j][k] = min(dp[j][k], dp[j][o] + dp[o+1][k] + info[j][0] * info[o][1] * info[k][1])

print(dp[0][-1])