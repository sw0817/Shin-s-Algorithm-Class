# 백준 1613 역사
# Baekjoon 1613

# Created by sw0817 on 2021. 12. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1613

from sys import stdin

def settingHistory(i):
    if visited[i]:
        return
    visited[i] = 1
    for v in events[i]:
        # v이전에 i가 일어남
        settingHistory(v)
        after[i].add(v)
        after[i] |= after[v]


n, k = map(int, stdin.readline().split())
events = [[] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    # a가 b보다 먼저 발생
    events[a].append(b)

after = [set() for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(n+1):
    settingHistory(i)

s = int(stdin.readline())
for _ in range(s):
    a, b = map(int, stdin.readline().split())
    if a in after[b]:
        print(1)
    elif b in after[a]:
        print(-1)
    else:
        print(0)