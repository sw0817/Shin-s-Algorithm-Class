# 백준 2887 행성 터널
# Baekjoon 2887

# Created by sw0817 on 2021. 10. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2887

from collections import defaultdict
import heapq

def prim(g, start):
    visited[start] = 1
    candidate = graph[start]
    heapq.heapify(candidate)
    mst = []
    total_weight = 0

    while candidate:
        w, u, v = heapq.heappop(candidate)
        if not visited[v]:
            visited[v] = 1
            mst.append((u, v))
            total_weight += w

            for e in g[v]:
                if not visited[e[2]]:
                    heapq.heappush(candidate, e)

    return total_weight


N = int(input())
info = []
for i in range(N):
    x, y, z = map(int, input().split())
    info.append((x, y, z, i))
graph = defaultdict(list)
visited = [0] * N

for i in range(3):
    info.sort(key=lambda x:x[i])
    for j in range(1, N):
        weight = abs(info[j-1][i] - info[j][i])
        u = info[j-1][3]
        v = info[j][3]
        graph[u].append([weight, u, v])
        graph[v].append([weight, v, u])

print(prim(graph, 0))