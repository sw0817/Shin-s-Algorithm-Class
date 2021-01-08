# 백준 15652 N과 M (4)
# Baekjoon 15652

# Created by sw0817 on 2021. 01. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15652

def make(n):
    if n == M:
        print(*nums)
        return

    for i in range(N):
        if visited[i]:
            continue
        nums.append(Ns[i])
        make(n+1)
        visited[i] = 1
        nums.pop()

        for j in range(i+1, N):
            visited[j] = 0


N, M = map(int, input().split())

nums = []
Ns = [i for i in range(1, N+1)]
visited = [0] * N
make(0)