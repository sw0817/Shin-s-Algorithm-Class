# 백준 2098 외판원 순회
# Baekjoon 2098

# Created by sw0817 on 2021. 08. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2098

def move(pre, state):
    if state == final:
        if arr[pre][0]:
            return arr[pre][0]

    if dp[state][pre]:
        return dp[state][pre]

    cost = INF
    for i in range(1, N):
        temp = state | (1 << i)
        if temp != state and arr[pre][i]:
            cost = min(cost, move(i, temp) + arr[pre][i])
    dp[state][pre] = cost
    return cost


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = 1000000 * N + 1
final = (1 << N) - 1
dp = [[0] * N for _ in range(1 << N)]

print(move(0, 1))
