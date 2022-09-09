# 백준 1633 최고의 팀 만들기
# Baekjoon 1633

# Created by sw0817 on 2022. 09. 10..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1633

info = []
l = 0

while True:
    try:
        b, w = map(int, input().split())
        info.append((b, w))
        l += 1
    except:
        break

dp = [[[0] * 16 for _ in range(16)] for _ in range(l+1)]
for i in range(l):
    for w in range(16):
        for b in range(16):
            if w < 15:
                dp[i+1][w+1][b] = max(dp[i+1][w+1][b], dp[i][w][b] + info[i][0])
            if b < 15:
                dp[i+1][w][b+1] = max(dp[i+1][w][b+1], dp[i][w][b] + info[i][1])
            dp[i+1][w][b] = max(dp[i+1][w][b], dp[i][w][b])

print(dp[l][15][15])