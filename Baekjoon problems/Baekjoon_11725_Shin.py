# 백준 11725 트리의 부모 찾기
# Baekjoon 11725

# Created by sw0817 on 2021. 05. 10..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11725

from sys import setrecursionlimit
setrecursionlimit(10 ** 5) # 10 ** 6 에선 메모리 초과


def dfs(v):
    visited[v] = 1
    for i in tree[v]:
        if not visited[i]:
            dic[i] = v
            dfs(i)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    t1, t2 = map(int, input().split())
    tree[t1].append(t2)
    tree[t2].append(t1)

visited = [0] * (N+1)

dic = dict()

dfs(1)
for i in range(2, N+1):
    if i in dic:
        print(dic[i])
    else:
        break