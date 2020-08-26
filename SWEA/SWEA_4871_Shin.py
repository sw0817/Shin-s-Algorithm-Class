# SWEA 4871 그래프 경로
# SWEA 4871

# Created by sw0817 on 2020. 08. 26..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def DFS(v, v2):
    visited[v] = 1
    for w in range(1, V+1):
        if visited[v2] == 1:
            return 1
        if Gr[v][w] == 1 and visited[w] == 0:
            DFS(w, v2)
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    Gr = [([0] * (V+1)) for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        Gr[a][b] = 1

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, DFS(S, G)))