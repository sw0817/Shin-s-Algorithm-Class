# 백준 1417 지능형 기차
# Baekjoon 1417

# Created by sw0817 on 2022. 11. 21..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1417

import heapq

queue = [0]
N = int(input())
c = int(input())

for _ in range(N-1):
    heapq.heappush(queue, -int(input()))

cnt = 0
while c <= -queue[0]:
    n = -heapq.heappop(queue)
    n -= 1
    cnt += 1
    c += 1
    heapq.heappush(queue, -n)

print(cnt)