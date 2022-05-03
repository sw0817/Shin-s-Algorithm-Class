# 백준 2780 비밀번호
# Baekjoon 2780

# Created by sw0817 on 2022. 05. 03..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2780

T = int(input())
Ns = []
for _ in range(T):
    Ns.append(int(input()))

N = max(Ns)
dp = [[1] * 10 for _ in range(N)]
case = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [4, 8, 0], [5, 7, 9], [6, 8]]
for i in range(1, N):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][c] for c in case[j]) % 1234567

for i in Ns:
    print(sum(dp[i-1]) % 1234567)