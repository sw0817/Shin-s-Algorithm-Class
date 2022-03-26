# 백준 2461 대표 선수
# Baekjoon 2461

# Created by sw0817 on 2022. 03. 26..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2461

import sys, heapq, math
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
students = [deque(sorted(list(map(int, input().split())))) for _ in range(N)]

heap = []

minV = math.inf
maxV = 0

for i in range(N):
    v = students[i].popleft()
    maxV = max(maxV, v)
    minV = min(minV, v)
    heapq.heappush(heap, [v, i])

dif = maxV - minV

while heap:
    preMinV, pos = heapq.heappop(heap)
    if not students[pos]:
        break

    newV = students[pos].popleft()
    heapq.heappush(heap, [newV, pos])

    maxV = max(maxV, newV)
    minV = heap[0][0]
    dif = min(dif, maxV - minV)

print(dif)