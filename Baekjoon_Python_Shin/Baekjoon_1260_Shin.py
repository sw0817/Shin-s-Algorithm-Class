# 백준 1260 DFS와 BFS
# Baekjoon 1260

# Created by sw0817 on 2021. 12. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1260

def dfs():
    v = stack.pop()
    print(v, end=' ')
    for n_v in adj[v]:
        if not visited[n_v]:
            visited[n_v] = 1
            stack.append(n_v)
            dfs()


def bfs():
    while queue:
        for _ in range(len(queue)):
            v = queue.pop(0)
            print(v, end=' ')
            add_queue = []
            for n_v in adj[v]:
                if not visited[n_v]:
                    visited[n_v] = 1
                    add_queue.append(n_v)
            queue.extend(sorted(add_queue))


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, N+1):
    adj[i] = list(set(adj[i]))
    adj[i].sort()

visited = [0] * (N+1)
visited[V] = 1

stack = [V]
queue = [V]

while stack:
    dfs()

print()
visited = [0] * (N+1)
visited[V] = 1

bfs()