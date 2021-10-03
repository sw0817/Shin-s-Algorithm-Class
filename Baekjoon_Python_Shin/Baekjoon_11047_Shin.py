# 백준 11047 동전 0
# Baekjoon 11047

# Created by sw0817 on 2021. 07. 01..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
result = 0
for i in range(N-1, -1, -1):
    result += K // coins[i]
    K = K % coins[i]
print(result)