# 백준 15481 그래프와 MST
# Baekjoon 15481

# Created by sw0817 on 2021. 01. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15481

from sys import stdin
from math import log2
from heapdict import heapdict


def prim(graph, start):
    keys = heapdict()

    pi = dict()

    total_weight = 0

    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        print(dict(keys))
        current_node, current_key = keys.popitem()
        print((current_node, current_key))
        depth[current_node] = depth[pi[current_node]] + 1
        mst_list[current_node][0] = pi[current_node]
        mst_list[current_node][1] = current_key

        total_weight += current_key

        for adjacent, weight in adj[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node

    return total_weight


V, E = map(int, stdin.readline().split())

edges = []
must = []

adj = {}
for i in range(1, V+1):
    adj[i] = {}

for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    edges.append([u, v, w])
    adj[u][v] = w
    adj[v][u] = w

depth = [0] * (V + 1)
mst_list = [[0, 0] for _ in range(V + 1)]
weight = prim(adj, 1)
mst_list[1][0] = 0

logV = int(log2(V)+1)

DP = [[[0, 0] for _ in range(logV)] for _ in range(V+1)]

for i in range(V+1):
    DP[i][0][0] = mst_list[i][0]
    DP[i][0][1] = mst_list[i][1]

for j in range(1, logV):
    for i in range(1, V+1):
        DP[i][j][0] = DP[DP[i][j-1][0]][j-1][0]
        DP[i][j][1] = max(DP[i][j-1][1], DP[DP[i][j-1][0]][j-1][1])

for edge in edges:
    if edge in must:
        print(weight)

    else:
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