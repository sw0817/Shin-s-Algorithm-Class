# 백준 1005 ACM Craft
# Baekjoon 1005

# Created by sw0817 on 2021. 06. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1005

from _collections import deque

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    loadings = [0] + list(map(int, input().split()))
    dp = [-1] * (N+1)
    tree = [[] for _ in range(N+1)]
    inDegree = [0] * (N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        tree[a].append(b)
        inDegree[b] += 1

    target = int(input())

    queue = deque()
    for i in range(1, N+1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = loadings[i]

    while queue:
        a = queue.popleft()
        for i in tree[a]:
            inDegree[i] -= 1
            dp[i] = max(dp[a]+loadings[i], dp[i])
            if inDegree[i] == 0:
                queue.append(i)

    print(dp[target])