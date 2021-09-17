# 백준 1176 섞기
# Baekjoon 1176

# Created by sw0817 on 2021. 09. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1176

def recur(status, last):
    if status == 2 ** N - 1:
        dp[status][last] = 1
        return 1

    ret = dp[status][last]
    if ret != 0:
        return ret

    ret = 0
    for i in range(N):
        if not status & (1 << i):
            if last == N or K < abs(arr[last] - arr[i]):
                ret += recur(status | (1 << i), i)

    dp[status][last] = ret
    return ret


N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [[0] * (N+1) for _ in range(1 << N + 1)]
recur(0, N)

print(dp[0][N])