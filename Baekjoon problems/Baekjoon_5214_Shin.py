# 백준 5214 환승
# Baekjoon 5214

# Created by sw0817 on 2021. 02. 27..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5214

from collections import deque

def check():
    queue = deque()
    queue.append(0)
    c[0] = 1
    while queue:
        x = queue.popleft()
        if x == N-1:
            return c[x]
        for v in adj[x]:
            if not c[v]:
                if v >= N:
                    c[v] = c[x]
                    queue.append(v)
                else:
                    c[v] = c[x] + 1
                    queue.append(v)
    return -1


N, K, M = map(int, input().split())
adj = [[] for _ in range(N+M)]
c = [0] * (N+M)
for _ in range(M):
    info = list(map(int, input().split()))
    for i in range(K):
        adj[info[i]-1].append(N+i)
        adj[N+i].append(info[i]-1)

print(check())