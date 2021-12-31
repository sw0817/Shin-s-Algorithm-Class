# 백준 5021 왕위 계승
# Baekjoon 5021

# Created by sw0817 on 2021. 12. 31..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5021

from collections import deque

N, M = map(int, input().split())
king = input()
children = dict()
point = dict()
info = []
for _ in range(N):
    names = list(map(str, input().split()))
    info.append(names)
    if not names[0] in children:
        children[names[0]] = []
    if names[1] in children:
        children[names[1]].append(names[0])
    else:
        children[names[1]] = [names[0]]
    if names[2] in children:
        children[names[2]].append(names[0])
    else:
        children[names[2]] = [names[0]]
    point[names[0]] = 0
    point[names[1]] = 0
    point[names[2]] = 0

candidates = []
for _ in range(M):
    candidates.append(input())

queue = deque()
queue.append(king)
cur = 1
while queue:
    for _ in range(len(queue)):
        parent = queue.popleft()
        for child in children[parent]:
            point[child] += cur / 2
            queue.append(child)
    cur /= 2

result = ''
cur = -1
for name in candidates:
    if not name in point:
        continue
    if cur < point[name]:
        cur = point[name]
        result = name

print(result)