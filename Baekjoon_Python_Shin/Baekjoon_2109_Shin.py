# 백준 2109 순회강연
# Baekjoon 2109

# Created by sw0817 on 2022. 01. 09..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2109

import heapq

n = int(input())
info = []
for _ in range(n):
    p, d = map(int, input().split())
    info.append([d, p])

info.sort()
queue = []
result = 0
for i in range(10000, 0, -1):
    while info and info[-1][0] == i:
        heapq.heappush(queue, -info.pop()[1])
    if queue:
        result += -heapq.heappop(queue)

print(result)
