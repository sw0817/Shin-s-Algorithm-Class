# 백준 4781 사탕가게
# Baekjoon 4781

# Created by sw0817 on 2021. 08. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4781

while True:
    N, M = map(float, input().split())
    N, M = int(N), int(M * 100 + 0.5)
    dp = [0] * (M+1)
    for i in range(1, N+1):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)
        for j in range(p, M+1):
            dp[j] = max(dp[j], dp[j-p] + c)

    if N == 0:
        break

    print(dp[M])