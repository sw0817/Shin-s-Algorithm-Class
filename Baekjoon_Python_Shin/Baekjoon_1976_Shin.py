# 백준 1976 여행 가자
# Baekjoon 1976

# Created by sw0817 on 2022. 04. 21..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1976

from collections import deque

def check():
    for i in range(1, len(trip)):
        t = trip[i] - 1
        queue = deque()
        queue.append(trip[0]-1)
        visited = [0] * N
        visited[trip[0]-1] = 1
        while queue and not possible[t]:
            n = queue.popleft()
            if n == t:
                possible[t] = 1
                break
            for v in adj[n]:
                if v == t:
                    possible[t] = 1
                    queue = deque()
                    break
                if possible[v] and not visited[v]:
                    queue.append(v)
                    visited[v] = 1
        if not possible[t]:
            return "NO"
    return "YES"


N = int(input())
M = int(input())
adj = [set() for _ in range(N)]
for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j]:
            adj[i].add(j)
            adj[j].add(i)

for i in range(N):
    adj[i] = list(adj[i])

trip = list(map(int, input().split()))
possible = [1] * N
for i in range(1, len(trip)):
    possible[trip[i]-1] = 0

print(check())

# 다시 풀기 .,asd