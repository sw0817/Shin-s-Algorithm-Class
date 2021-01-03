# 백준 3176 도로 네트워크
# Baekjoon 3176

# Created by sw0817 on 2020. 01. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3176

from _collections import deque
from math import log2
from sys import stdin

N = int(stdin.readline())

adj = [[] for _ in range(N+1)]
depth = [0] * (N+1)
logN = int(log2(N)+1)
for _ in range(N-1):
    v1, v2, l = map(int, stdin.readline().split())
    adj[v1].append([v2, l])
    adj[v2].append([v1, l])

mst_list = [[0, 0] for _ in range(N+1)]
mst = [False] * (N+1)
queue = deque()
queue.append(1)
mst[1] = True
while queue:
    v = queue.popleft()
    for v2, l in adj[v]:
        if not mst[v2]:
            queue.append(v2)
            depth[v2] = depth[v] + 1
            mst[v2] = True
            mst_list[v2][0] = v
            mst_list[v2][1] = l

# 2^k 번째 부모 노드와 가장 짧은 도로, 가장 긴 도로
DP = [[[0, 0, 0] for _ in range(logN)] for _ in range(N+1)]

# 초기 설정
for i in range(N+1):
    DP[i][0][0] = mst_list[i][0]
    DP[i][0][1] = mst_list[i][1]
    DP[i][0][2] = mst_list[i][1]

# 희소테이블
for j in range(1, logN):
    for i in range(1, N+1):
        DP[i][j][0] = DP[DP[i][j-1][0]][j-1][0]
        DP[i][j][1] = min(DP[i][j-1][1], DP[DP[i][j-1][0]][j-1][1])
        DP[i][j][2] = max(DP[i][j-1][2], DP[DP[i][j-1][0]][j-1][2])

K = int(stdin.readline())
INF = 1000001
for _ in range(K):
    D, E = map(int, stdin.readline().split())
    if depth[D] < depth[E]:
        D, E = E, D

    dif = depth[D] - depth[E]
    shortest = INF
    longest = 0

    # 뎁스 맞추기
    for i in range(logN):
        if dif & 1 << i:
            shortest = min(shortest, DP[D][i][1])
            longest = max(longest, DP[D][i][2])
            D = DP[D][i][0]

    if D == E:
        print(shortest, longest)

    else:
        # 최소 공통 조상 찾기
        for i in range(logN-1, -1, -1):
            if DP[D][i][0] != DP[E][i][0]:
                shortest = min(shortest, DP[D][i][1], DP[E][i][1])
                longest = max(longest, DP[D][i][2], DP[E][i][2])
                D = DP[D][i][0]
                E = DP[E][i][0]

        shortest = min(shortest, DP[D][i][1], DP[E][i][1])
        longest = max(longest, DP[D][i][2], DP[E][i][2])
        print(shortest, longest)