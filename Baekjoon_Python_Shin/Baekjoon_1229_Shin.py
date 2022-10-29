# 백준 1229 육각수
# Baekjoon 1229

# Created by sw0817 on 2022. 10. 29..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1229

def cal(lmt):
    n = 1
    cur = 0
    ret = []
    while cur <= lmt:
        cur = n * (2 * n - 1)
        ret.append(cur)
        n += 1

    return ret[:-1]


N = int(input())
dp = [i for i in range(6)] + [i for i in range(1, 7)] + [2] + [float('inf')] * 1000000

if N < 13:
    print(dp[N])
else:
    hex = cal(N)
    for i in range(13, N + 1):
        min_v = float('inf')
        for h in hex:
            if i < h:
                break
            min_v = min(min_v, dp[i - h])
        dp[i] = min_v + 1
    print(dp[N])
