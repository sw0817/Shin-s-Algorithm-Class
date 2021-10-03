# 백준 1202 보석 도둑
# Baekjoon 1202

# Created by sw0817 on 2020. 12. 09..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1202

import sys
from queue import PriorityQueue

N, K = map(int, sys.stdin.readline().split())

juwels = []
bags = []

for _ in range(N):
    juwels.append(list(map(int, sys.stdin.readline().split())))

for _ in range(K):
    bags.append(int(sys.stdin.readline()))

juwels.sort(key=lambda item: item[1], reverse=True)

for i in range(N):
    juwels[i].insert(0, i)

juwels.sort(key=lambda item: item[1])
bags.sort()
queue = PriorityQueue()

result = 0
idx = 0

for i in range(K):
    while idx < N and bags[i] >= juwels[idx][1]:
        queue.put((juwels[idx][0], juwels[idx][2]))

        idx += 1
    if not queue.empty():
        result += queue.get()[1]

print(result)
