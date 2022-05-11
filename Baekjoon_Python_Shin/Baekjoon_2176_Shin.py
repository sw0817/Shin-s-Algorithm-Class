# 백준 2176 합리적인 이동경로
# Baekjoon 2176

# Created by sw0817 on 2022. 05. 11..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2176

from sys import stdin
import math
import heapq

def dijsktra(s):
    dist = [inf] * (N+1)
    dist[s] = 0
    hq = []
    heapq.heappush(hq, [0, s])

    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue

        for nxt_node, nxt_cost in nodes[node]:
            if cost + nxt_cost < dist[nxt_node]:
                dist[nxt_node] = cost + nxt_cost
                heapq.heappush(hq, [cost + nxt_cost, nxt_node])

    return dist


def good_path(node):
    if not dp[node]:
        for nxt_node, nxt_cost in nodes[node]:
            if dist[nxt_node] < dist[node]:
                dp[node] += good_path(nxt_node)
        return dp[node]
    else:
        return dp[node]


inf = math.inf
input = stdin.readline

N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    nodes[A].append([B, C])
    nodes[B].append([A, C])

dp = [0] * (N+1)
dp[2] = 1
dist = dijsktra(2)

print(good_path(1))