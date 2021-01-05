# 백준 15481 그래프와 MST
# Baekjoon 15481

# Created by sw0817 on 2020. 01. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15481

from sys import stdin
from math import log2
from _collections import defaultdict
from heapq import *


V, E = map(int, stdin.readline().split())

mst = list()
edges = defaultdict(list)
final = []

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    final.append([u, v, w])
    edges[u].append((w, u, v))
    edges[v].append((w, v, u))

depth = [0] * (V + 1)
mst_list = [[0, 0] for _ in range(V + 1)]
weight = 0

connected_nodes = set([1])
candidate_edge_list = edges[1]
heapify(candidate_edge_list)
while candidate_edge_list:

    w, u, v = heappop(candidate_edge_list)
    if v not in connected_nodes:
        weight += w
        mst_list[v][0] = u
        mst_list[v][1] = w
        depth[v] = depth[u] + 1
        connected_nodes.add(v)
        mst.append((w, u, v))

        for edge in edges[v]:
            if edge[2] not in connected_nodes:
                heappush(candidate_edge_list, edge)

logV = int(log2(V)+1)

DP = [[[0, 0] for _ in range(logV)] for _ in range(V+1)]

for i in range(V+1):
    DP[i][0][0] = mst_list[i][0]
    DP[i][0][1] = mst_list[i][1]

for j in range(1, logV):
    for i in range(1, V+1):
        DP[i][j][0] = DP[DP[i][j-1][0]][j-1][0]
        DP[i][j][1] = max(DP[i][j-1][1], DP[DP[i][j-1][0]][j-1][1])

for edge in final:

    D, E = edge[0], edge[1]
    if depth[D] < depth[E]:
        D, E = E, D

    dif = depth[D] - depth[E]
    longest = 0

    for i in range(logV):
        if dif & 1 << i:
            longest = max(longest, DP[D][i][1])
            D = DP[D][i][0]

    if D == E:
        print(weight - longest + edge[2])

    else:
        for i in range(logV-1, -1, -1):
            if DP[D][i][0] != DP[E][i][0]:
                longest = max(longest, DP[D][i][1], DP[E][i][1])
                D = DP[D][i][0]
                E = DP[E][i][0]

        longest = max(longest, DP[D][i][1], DP[E][i][1])
        print(weight - longest + edge[2])