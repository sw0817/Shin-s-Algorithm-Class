# 백준 15481 그래프와 MST
# Baekjoon 15481

# Created by sw0817 on 2020. 01. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15481

V, E = map(int, input().split())

adj = [[] for _ in range(V)]
must = []
for _ in range(E):
    v1, v2, n = map(int, input().split())
    adj[v1-1].append((v2-1, n))
    adj[v2-1].append((v1-1, n))
    must.append((v1-1, v2-1, n))

INF = 10 ** 9 + 1

for i in range(E):
    key = [INF] * V
    mst = [False] * V

    v1, v2, n = must[i]

    key[v1] = 0
    key[v2] = 0
    mst[v1] = True
    mst[v2] = True

    for w, n2 in adj[v1]:
        if not mst[w] and key[w] > n2:
            key[w] = n2

    for w, n2 in adj[v2]:
        if not mst[w] and key[w] > n2:
            key[w] = n2

    result = n
    cnt = 2

    while cnt <= V-1:
        minV = INF
        minIdx = 0
        for i in range(V):
            if not mst[i] and minV > key[i]:
                minV = key[i]
                minIdx = i
        mst[minIdx] = True
        result += minV
        cnt += 1

        for w, n in adj[minIdx]:
            if not mst[w] and key[w] > n:
                key[w] = n

    print(result)