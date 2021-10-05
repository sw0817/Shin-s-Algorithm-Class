# 백준 1219 오민식의 고민
# Baekjoon 1219

# Created by sw0817 on 2021. 10. 05..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1219

import math
from collections import deque

def continueSum(V):
    visited = [0] * N
    queue = deque([V])
    while queue:
        v = queue.popleft()
        if v == E:
            return True
        visited[v] = 1
        for v2, cost in adj[v]:
            if not visited[v2]:
                queue.append(v2)
    return False


N, S, E, M = map(int, input().split())
adj = [[] for _ in range(N)]
nodes = [-math.inf] * N
result = 0

for _ in range(M):
    s, e, cost = map(int, input().split())
    adj[s].append([e, cost])

costs = list(map(int, input().split()))
nodes[S] = costs[S]
for i in range(N):
    for v in adj[i]:
        v[1] = costs[v[0]] - v[1]

bellmanFord = True
for i in range(N+1):
    if not bellmanFord:
        break

    if nodes[E] == -math.inf and i == N:
        bellmanFord = False
        print('gg')
        break

    for j in range(N):
        if not bellmanFord:
            break

        if nodes[j] == -math.inf:
            continue

        for e, cost in adj[j]:
            if not bellmanFord:
                break
            if nodes[j] + cost > nodes[e]:
                nodes[e] = nodes[j] + cost
                if i == N and continueSum(e):
                    print('Gee')
                    bellmanFord = False
                    break

if bellmanFord:
    print(nodes[E])