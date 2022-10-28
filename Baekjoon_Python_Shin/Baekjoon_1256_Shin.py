# 백준 1256 사전
# Baekjoon 1256

# Created by sw0817 on 2022. 10. 28..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1256

N, M, K = map(int, input().split())
dp = [[1]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[N][M] < K:
    print(-1)
else:
    result = ''

    while True:
        if N == 0 or M == 0:
            result += 'a' * N + 'z' * M
            break

        cnt = dp[N-1][M]
        if cnt >= K:
            result += 'a'
            N -= 1
        else:
            result += 'z'
            M -= 1
            K -= cnt

    print(result)