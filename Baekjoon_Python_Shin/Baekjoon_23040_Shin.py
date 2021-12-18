# 백준 23040 누텔라 트리 (Easy)
# Baekjoon 23040

# Created by sw0817 on 2021. 12. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/23040

from collections import deque

def dfs(v):
    visited[v] = 1
    ret = dp[v] if dp[v] else 1
    cur.append(v)
    if 1 < ret:
        return
    for n_v in adj[v]:
        if not visited[n_v] and black[n_v-1] == 'R':
            if not dp[n_v]:
                dfs(n_v)
            ret += dp[n_v]

    visited[v] = 0
    dp[v] = ret


N = int(input())
result = 0
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited = [0] * (N+1)
dp = [0] * (N+1)
black = input()

for i in range(1, N+1):
    if black[i-1] == 'B':
        visited[i] = 1
        for v in adj[i]:
            if black[v-1] == 'B':
                continue
            if not dp[v]:
                cur = deque()
                dfs(v)
            n = dp[v]
            while cur:
                v = cur.popleft()
                dp[v] = n
            result += dp[v]

print(result)