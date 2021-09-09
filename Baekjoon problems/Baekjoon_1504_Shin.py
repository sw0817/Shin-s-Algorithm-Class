# 백준 1504 특정한 최단 경로
# Baekjoon 1504

# Created by sw0817 on 2021. 09. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1504

from heapq import heappush, heappop

def dijkstra(start):
    dp = [INF] * (N+1)
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, c = heappop(heap)
        for v, new_w in adj[c]:
            weight = new_w + w
            if weight < dp[v]:
                dp[v] = weight
                heappush(heap, [weight, v])
    return dp


N, E = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, input().split())
INF = 987654321
# 1 -> v1 -> v2 -> N
# 1 -> v2 -> v1 -> N
# 이 두 가지 최단거리를 구해본다.
start_lst = dijkstra(1)
v1_lst = dijkstra(v1)
v2_lst = dijkstra(v2)

cnt = min(start_lst[v1] + v1_lst[v2] + v2_lst[N], start_lst[v2] + v2_lst[v1] + v1_lst[N])
print(cnt if cnt < INF else -1)