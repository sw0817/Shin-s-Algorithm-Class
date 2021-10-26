# 백준 2618 경찰차
# Baekjoon 2618

# Created by sw0817 on 2021. 10. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2618

N = int(input())
W = int(input())
accident = []
dp = [[0] * (W+1) for _ in range(W+1)]
for i in range(W):
    info = list(map(int, input().split()))
    accident.append(info)

dp[1][0] = accident[0][0] + accident[0][1] - 2
dp[0][1] = abs(N - accident[0][0]) + abs(N - accident[0][1])
for i in range(1, W):
    dp[i+1][0] = dp[i][0] + abs(accident[i][0] - accident[i-1][0]) + abs(accident[i][1] - accident[i-1][1])
    dp[0][i+1] = dp[0][i] + abs(accident[i][0] - accident[i-1][0]) + abs(accident[i][1] - accident[i-1][1])

for i in range(1, W+1):
    for j in range(1, W+1):
        pass

# DP 테이블 설계 중