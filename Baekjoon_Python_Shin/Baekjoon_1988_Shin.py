# 백준 1988 낮잠 시간
# Baekjoon 1988

# Created by sw0817 on 2021. 10. 05..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1988

N, B = map(int, input().split())
dp = [[0] * 3 for _ in range(N+1)]
nxt = [[0] * 3 for _ in range(N+1)]
result = 0

for i in range(N):
    recovery = int(input())
    for j in range(B+1):
        nxt[j][0] = max(dp[j][0], dp[j][1], dp[j][2])
        nxt[j][1] = dp[j-1][0] if j else -1
        nxt[j][2] = -1

        if 1 < j and dp[j-1][1] != -1:
            nxt[j][2] = dp[j-1][1] + recovery
        if 1 < j and dp[j-1][2] != -1:
            nxt[j][2] = max(nxt[j][2], dp[j-1][2] + recovery)

    dp, nxt = nxt, dp
    result = max(result, dp[B][0], dp[B][1], dp[B][2])

print(result)