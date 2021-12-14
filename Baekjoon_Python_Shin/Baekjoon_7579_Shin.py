# 백준 7579 앱
# Baekjoon 7579

# Created by sw0817 on 2021. 12. 14..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/7579

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
max_cost = sum(costs)
dp = [0] * (max_cost + 1)
for i in range(N):
    for j in range(max_cost, costs[i]-1, -1):
        dp[j] = max(dp[j], dp[j-costs[i]] + memories[i])

for i in range(max_cost+1):
    if M <= dp[i]:
        print(i)
        break