# 백준 1246 온라인 판매
# Baekjoon 1246

# Created by sw0817 on 2022. 09. 15..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1246

N, M = map(int, input().split())
cost = []
for _ in range(M):
    cost.append(int(input()))

cost.sort(reverse=True)
result = 0
c = 0
for i in range(min(M, N)):
    cur = (i+1) * cost[i]
    if result <= cur:
        result = cur
        c = cost[i]

print(c, result)