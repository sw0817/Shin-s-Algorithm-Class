# 백준 17352 여러분의 다리가 되어 드리겠습니다!
# Baekjoon 17352

# Created by sw0817 on 2021. 12. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17352

from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0] * (N+1)
visited[1] = 1
queue = deque()
queue.append(1)
while queue:
    n = queue.popleft()
    for v in adj[n]:
        if not visited[v]:
            visited[v] = 1
            queue.append(v)

for i in range(2, N+1):
    if not visited[i]:
        print(1, i)
        break