# 백준 9466 텀 프로젝트
# Baekjoon 9466

# Created by sw0817 on 2021. 12. 02..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9466

import sys
sys.setrecursionlimit(10 ** 6)

def recur(x):
    global result
    visited[x] = 1
    cycle.append(x)
    n = info[x]

    if visited[n]:
        if n in cycle:
            result += cycle[cycle.index(n):]
        return
    else:
        recur(n)


for _ in range(int(input())):
    N = int(input())
    info = [0] + list(map(int, input().split()))
    visited = [1] + [0] * N
    result = []

    for i in range(1, N + 1):
        if not visited[i]:
            cycle = []
            recur(i)

    print(N - len(result))