# 백준 16876 재미있는 숫자 게임
# Baekjoon 16876

# Created by sw0817 on 2022. 01. 01..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/16876

def recur(t, n):
    num = int(n)
    if t == M:
        if t % 2:
            if int(N) < num:
                return 0
            else:
                return 1
        else:
            if int(N) < num:
                return 1
            else:
                return 0

    if dp[num][t] != -1:
        return dp[num][t]

    dp[num][t] = 0
    for i in range(4):
        cur = int(n[i])
        if cur == 9:
            nxt = n[:i] + '0' + n[i+1:]
        else:
            nxt = n[:i] + str(cur+1) + n[i+1:]

        if not recur(t+1, nxt):
            dp[num][t] = 1

    return dp[num][t]


N, M = map(str, input().split())
M = int(M)
# i인 상황에서 j턴일 때 승패여부
dp = [[-1] * (M+1) for _ in range(10000)]
if recur(0, N):
    print('koosaga')
else:
    print('cubelover')