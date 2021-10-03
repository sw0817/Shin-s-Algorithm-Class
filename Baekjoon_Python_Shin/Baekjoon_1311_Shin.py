# 백준 1311 할 일 정하기 1
# Baekjoon 1311

# Created by sw0817 on 2021. 09. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1311

def check(state, idx):
    if state == bit - 1:
        return 0

    if dp[idx][state] != -1:
        return dp[idx][state]

    dp[idx][state] = INF

    for i in range(N):
        if state & (1 << i):
            continue
        dp[idx][state] = min(dp[idx][state], check(state | (1 << i), idx + 1) + arr[idx][i])

    return dp[idx][state]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

bit = 2 ** N
INF = 10000 * 20
dp = [[-1] * bit for _ in range(N)]

check(0, 0)

print(dp[0][0])