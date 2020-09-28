# SWEA 5102 노드의 거리
# SWEA 5102

# Created by sw0817 on 2020. 09. 28..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def bfs2(v):
    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.pop(0)
        for w in Gr[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1


T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    Gr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        Gr[temp[i][0]].append(temp[i][1])
        Gr[temp[i][1]].append(temp[i][0])

    bfs2(S)

    if visited[G] != 0:
        print('#{} {}'.format(tc, visited[G]-1))
    else:
        print('#{} 0'.format(tc))