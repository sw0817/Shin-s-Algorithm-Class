# 백준 11404 플로이드
# Baekjoon 11404

# Created by sw0817 on 2021. 04. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11404

n = int(input())
m = int(input())
INF = 99999999999
adj = [[INF] * (n+1) for _ in range(n+1)]
dp = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < adj[a][b]:
        adj[a][b] = c
        dp[a][b] = c

for i in range(1, n+1):
    adj[i][i] = 0
    dp[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == INF:
            print(0, end=' ')
        else:
            print(dp[i][j], end=' ')
    print()