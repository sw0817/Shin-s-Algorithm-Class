# 백준 1967 트리의 지름
# Baekjoon 1967

# Created by sw0817 on 2021. 08. 10..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1967

from collections import deque

n = int(input())
parents = [[] for _ in range(n+1)]
children = [[] for _ in range(n+1)]
up = [[0, 0] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    parents[c].append(p)
    parents[c].append(w)
    children[p].append(c)

result = [[] for _ in range(n+1)]
queue = deque()
for i in range(1, n+1):
    if not children[i]:
        queue.append(i)

while queue:
    c = queue.popleft()
    if c == 1:
        continue
    p, w = parents[c]
    up[p][0] += 1
    result[p].append(up[c][1] + w)
    up[p][1] = max(up[p][1], up[c][1] + w)
    if up[p][0] == len(children[p]):
        queue.append(p)

for i in range(1, n+1):
    result[i].sort(reverse=True)
    result[i] = sum(result[i][:2])

print(max(result[1:]))