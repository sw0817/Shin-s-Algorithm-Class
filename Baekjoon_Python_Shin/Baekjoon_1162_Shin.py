# 백준 1162 도로포장
# Baekjoon 1162

# Created by sw0817 on 2022. 09. 29..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1162

import heapq

def dijxstr(s):
    queue = []
    cnt = 0
    dp[s][cnt] = 0
    heapq.heappush(queue, (0, s, cnt))

    while queue:
        w, n, cnt = heapq.heappop(queue)
        if not dp[n][cnt] < w:
            for c, n_n in adj[n]:
                n_w = w + c
                if dp[n_n][cnt] > n_w:
                    dp[n_n][cnt] = n_w
                    heapq.heappush(queue, (n_w, n_n, cnt))

                if cnt < K and dp[n_n][cnt+1] > w:
                    dp[n_n][cnt+1] = w
                    heapq.heappush(queue, (w, n_n, cnt+1))


N, M, K = map(int, input().split())
dp = [[float('inf')] * (K+1) for _ in range(N+1)]
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    adj[s].append((c, e))
    adj[e].append((c, s))

dijxstr(1)
print(min(dp[N]))