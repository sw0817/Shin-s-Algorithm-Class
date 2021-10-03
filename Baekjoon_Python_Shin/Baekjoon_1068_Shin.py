# 백준 1068 트리
# Baekjoon 1068

# Created by sw0817 on 2021. 08. 01..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1068

from collections import deque

def check(n):
    l = len(child[n])
    for i in range(l):
        if not child[n][i] in none:
            return 0
    return 1


N = int(input())
parents = list(map(int, input().split()))
child = [[] for _ in range(N)]
for i in range(N):
    if parents[i] == -1:
        continue
    child[parents[i]].append(i)

none = set()
D = int(input())

queue = deque()
queue.append(D)
while queue:
    d = queue.popleft()
    none.add(d)
    for c in child[d]:
        queue.append(c)

result = 0
for i in range(N):
    if not i in none:
        result += check(i)

print(result)