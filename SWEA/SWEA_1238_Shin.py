# SWEA 1238 Contact
# SWEA 1238

# Created by sw0817 on 2020. 09. 24..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD&categoryId=AV15B1cKAKwCFAYD&categoryType=CODE


def bfs2(v):
    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1


for tc in range(1, 11):

    N, R = map(int, input().split())
    V = 100
    temp = list(map(int, input().split()))
    result = 0
    G = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(N//2):
        s, e = temp[2*i], temp[2*i+1]
        G[s].append(e)

    bfs2(R)
    maxI = 0
    for i in range(1, V+1):
        if visited[maxI] < visited[i]:
            maxI = i

    for j in range(1, V+1):
        if visited[maxI] == visited[j]:
            if result < j:
                result = j
                
    print('#{} {}'.format(tc, result))