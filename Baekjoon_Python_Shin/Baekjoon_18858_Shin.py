# 백준 18858 훈련소로 가는 날
# Baekjoon 18858

# Created by sw0817 on 2021. 12. 19..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/18858

def cal(n, m, dir):
    ret = dp[n][m][dir]
    if ret != -1:
        return ret
    if n == N + 1:
        ret = 1
        return ret

    ret = 0

    if dir == 2:
        ret += cal(n + 1, m, 0)
        ret %= mod
        for i in range(m + 1, M + 1):
            ret += cal(n + 1, i, 2)
            ret %= mod
    else:
        for i in range(1, m):
            ret += cal(n+1, i, 1)
            ret %= mod
        ret += cal(n+1, m, 0)
        ret %= mod
        for i in range(m+1, M+1):
            ret += cal(n+1, i, 2)
            ret %= mod

    dp[n][m][dir] = ret
    return ret


N, M = map(int, input().split())
dp = [[[-1] * 3 for _ in range(M+2)] for _ in range(N+2)]
mod = 998244353

ret = 0
for i in range(1, M+1):
    ret += cal(2, i, 0)
    ret %= mod

print(ret)