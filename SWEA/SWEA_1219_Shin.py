# SWEA 1219 길찾기
# SWEA 1219

# Created by sw0817 on 2020. 08. 17..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD&categoryId=AV14geLqABQCFAYD&categoryType=CODE


T, N = map(int, input().split())

def dfs(v):
    s = []
    s.append(v)
    while len(s) != 0:
        v = s.pop()
        if not visited[v]:
            visited[v] = 1
            if G[v][99] == 1:
                return 1
            for w in range(100):
                if G[v][w] == 1 and visited[w] == 0:
                    s.append(w)
    return 0

for _ in range(10):
    T, N = map(int, input().split())
    node = list(map(int, input().split()))
    G = [([0] * 100) for _ in range(100)]
    visited = [0] * 100
    for i in range(0, 2 * N, 2):
        G[node[i]][node[i+1]] = 1


    print('#{} {}'.format(T, dfs(0)))
