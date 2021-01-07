# 백준 15481 그래프와 MST
# Baekjoon 15481

# Created by sw0817 on 2021. 01. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15481

from sys import stdin
from _collections import deque
from math import log2


V, E = map(int, stdin.readline().split())

edges = []

weight = 0

for _ in range(E):
    edges.append(list(map(int, stdin.readline().split())))

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root2] < rank[root1]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal():
    global weight
    for v in range(1, V+1):
        make_set(v)

    kru_edges = sorted(edges, key=lambda x : x[2])

    for v, u, w in kru_edges:
        if find(v) != find(u):
            union(v, u)
            adj[v].append([u, w])
            adj[u].append([v, w])
            weight += w

adj = [[] for _ in range(V+1)]
depth = [0] * (V+1)
logV = int(log2(V)+1)
mst_list = [[0, 0] for _ in range(V+1)]
mst = [False] * (V+1)

kruskal()

queue = deque()
queue.append(1)
mst[1] = True
while queue:
    v = queue.popleft()
    for v2, w in adj[v]:
        if not mst[v2]:
            queue.append(v2)
            depth[v2] = depth[v] + 1
            mst[v2] = True
            mst_list[v2][0] = v
            mst_list[v2][1] = w

DP = [[[0, 0] for _ in range(logV)] for _ in range(V+1)]

for i in range(V+1):
    DP[i][0][0] = mst_list[i][0]
    DP[i][0][1] = mst_list[i][1]

for j in range(1, logV):
    for i in range(1, V+1):
        DP[i][j][0] = DP[DP[i][j-1][0]][j-1][0]
        DP[i][j][1] = max(DP[i][j-1][1], DP[DP[i][j-1][0]][j-1][1])

for edge in edges:

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