# 백준 10423 전기가 부족해
# Baekjoon 10423

# Created by sw0817 on 2021. 08. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10423

N, M, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
active = [False] * (N+1)
active_num = list(map(int, input().split()))
cnt = 0
for n in active_num:
    active[n] = True
    cnt += 1
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

INF = 10001
result = 0
while cnt < N:
    cur = INF
    idx = 0
    for i in range(1, N+1):
        if not active[i]:
            for v, w in adj[i]:
                if active[v] and w < cur:
                    cur = w
                    idx = i
    result += cur
    active[idx] = True
    cnt += 1

print(result)