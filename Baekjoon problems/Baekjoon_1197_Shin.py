# 백준 1197 최소 스패닝 트리
# Baekjoon 1197

# Created by sw0817 on 2020. 01. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1197

V, E = map(int, input().split())

adj = [[] for _ in range(V)]

for i in range(E):
    v1, v2, n = map(int, input().split())
    adj[v1-1].append((v2-1, n))
    adj[v2-1].append((v1-1, n))

INF = 2147483648
key = [INF] * V
mst = [False] * V

key[0] = 0
cnt = 0
result = 0

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