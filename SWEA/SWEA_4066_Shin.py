# SWEA 4066 [Professional] All Pair Shortest Path
# SWEA 4066

# Created by sw0817 on 2021. 04. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 플로이드 워셜
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    INF = 99999999999
    adj = [[] for _ in range(N+1)]
    dp = [[INF] * (N+1) for _ in range(N+1)]
    adj2 = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        if c < adj2[a][b]:
            adj2[a][b] = c
            dp[a][b] = c

    for i in range(N+1):
        adj2[i][i] = 0
        dp[i][i] = 0

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    print('#{}'.format(tc), end=' ')
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dp[i][j] == INF:
                print(-1, end=' ')
            else:
                print(dp[i][j], end=' ')
    print()