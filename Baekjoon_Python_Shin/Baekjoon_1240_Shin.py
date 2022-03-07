# 백준 1240 노드사이의 거리
# Baekjoon 1240

# Created by sw0817 on 2022. 03. 07..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1240

def cal(v, l):
    if v == e:
        print(l)
        return

    for n_v, n_l in adj[v]:
        if not visited[n_v]:
            visited[n_v] = 1
            cal(n_v, l + n_l)
            visited[n_v] = 0


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e, l = map(int, input().split())
    adj[s].append([e, l])
    adj[e].append([s, l])

for _ in range(M):
    s, e = map(int, input().split())
    visited = [0] * (N+1)
    visited[s] = 1
    cal(s, 0)