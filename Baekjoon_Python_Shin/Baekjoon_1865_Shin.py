# 백준 1865 웜홀
# Baekjoon 1865

# Created by sw0817 on 2021. 01. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1865

def worm():
    for i in range(N):
        for v in range(1, N+1):
            for e, t in roads[v]:
                if visited[v] + t < visited[e]:
                    visited[e] = visited[v] + t
                    if i == N-1:
                        print('YES')
                        return
    print('NO')
    return


Tc = int(input())

for _ in range(Tc):
    N, M, W = map(int, input().split())
    roads = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        roads[S].append([E, T])
        roads[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        roads[S].append([E, -T])

    INF = 10000 * 2500
    visited = [INF] * (N+1)
    visited[1] = 0
    worm()
