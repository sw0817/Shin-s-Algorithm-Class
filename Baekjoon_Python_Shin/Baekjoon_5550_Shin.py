# 백준 5550 헌책방
# Baekjoon 5550

# Created by sw0817 on 2021. 11. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5550

N, K = map(int, input().split())
genre = [[] for _ in range(11)]
cost = [[0] * (N+1) for _ in range(11)]
for _ in range(N):
    C, G = map(int, input().split())
    genre[G].append(C)

for i in range(1, 11):
    genre[i].sort(reverse=True)
    l = len(genre[i])
    cur = 0
    for j in range(l):
        cur += genre[i][j] + ((j+1) * j - j * (j-1))
        cost[i][j+1] = cur

# dp[i][j] = i장르까지 j개 책 읽었을 때 최대
dp = [[0] * (K+1) for _ in range(11)]
for i in range(1, 11):
    for j in range(1, K+1):
        for k in range(j+1):
            dp[i][j] = max(dp[i][j], dp[i-1][k] + cost[i][j-k])

print(dp[10][K])