# 백준 2666 벽장문의 이동
# Baekjoon 2666

# Created by sw0817 on 2022. 10. 11..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2666

def solve(idx, d1, d2):
    if idx == l:
        return 0
    d_idx = ordr[idx]
    dp[d_idx][d1][d2] = min(abs(d1 - d_idx) + solve(idx+1, d_idx, d2), abs(d2 - d_idx) + solve(idx+1, d1, d_idx))
    return dp[d_idx][d1][d2]


N = int(input())
d1, d2 = map(int, input().split())
l = int(input())
ordr = []
dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]
for _ in range(l):
    ordr.append(int(input()))

print(solve(0, d1, d2))