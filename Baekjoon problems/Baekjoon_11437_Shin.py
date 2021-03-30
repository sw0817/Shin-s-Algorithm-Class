# 백준 11437 LCA
# Baekjoon 11437

# Created by sw0817 on 2021. 03. 29..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11437

from math import log2, floor
import sys

sys.setrecursionlimit(10**5)

def tree(cur, parent):

    # 현재 노드 깊이는 부모 깊이 + 1
    depth[cur] = depth[parent] + 1

    # 현재 노드 2^0 조상은 부모
    dp[cur][0] = parent

    # 루트까지 2^i 번째 조상을 찾아 dp에 넣는다.
    for i in range(1, max_depth+1):
        temp = dp[cur][i-1]
        dp[cur][i] = dp[temp][i-1]

    # 자식을 부모로 하는 노드에 대해서도 처리
    l = len(adj[cur])
    for i in range(l):
        target = adj[cur][i]

        # 부모 여부는 부모가 먼저 함수로 들어오게 되어있음.
        if target != parent:
            tree(target, cur)


N = int(input())

# 양방향 그래프 (트리)
adj = [[] for _ in range(N+1)]

# 노드 깊이
depth = [-1] * (N+1)

# 최대 깊이
max_depth = floor(log2(N+1))

# x의 2^y번째 조상
dp = [[0] * (max_depth+1) for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

tree(1, 0)

M = int(input())
for _ in range(M):

    # 두 노드를 같은 깊이로 맞추고 동시에 깊이를 하나씩 올려 공통조상을 찾는다.
    n1, n2 = map(int, input().split())

    # 깊이를 맞춘다.
    if depth[n1] != depth[n2]:

        # n2가 더 깊은 depth를 가지게 세팅
        if depth[n2] < depth[n1]:
            n1, n2 = n2, n1

        # 깊이가 같아질 때까지 n2의 조상을 타고 올린다.
        for i in range(max_depth, -1, -1):
            if depth[n1] <= depth[dp[n2][i]]:
                n2 = dp[n2][i]

    lca = n1

    # 현재 같은 깊이에서 두 노드의 조상이 같아질때까지 올라가 확인
    if n1 != n2:
        for i in range(max_depth, -1, -1):
            if dp[n1][i] != dp[n2][i]:
                n1 = dp[n1][i]
                n2 = dp[n2][i]

            lca = dp[n1][i]

    print(lca)