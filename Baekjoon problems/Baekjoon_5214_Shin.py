# 백준 5214 환승
# Baekjoon 5214

# Created by sw0817 on 2021. 02. 27..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5214

from collections import deque

def check():
    if N == 1:
        return 1

    if N in adj[1]:
        return 2

    else:
        queue = deque()
        cnt = 2
        visited = [0] * (N + 1)
        visited[1] = 1
        for st in adj[1]:
            queue.append(st)
            visited[st] = 1

        while queue:
            cnt += 1
            for _ in range(len(queue)):
                v = queue.popleft()
                for w in adj[v]:
                    if not visited[w]:
                        if w == N:
                            return cnt
                        visited[w] = 1
                        queue.append(w)

        return -1


N, K, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    info = list(map(int, input().split()))
    for i in range(K-1):
        for j in info[i+1:]:
            adj[info[i]].append(j)
            adj[j].append(info[i])

print(check())