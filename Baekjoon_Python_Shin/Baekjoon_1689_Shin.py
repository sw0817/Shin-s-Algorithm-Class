# 백준 1689 겹치는 선분
# Baekjoon 1689

# Created by sw0817 on 2022. 03. 23..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1689

import heapq

N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
lines.sort()
queue = []
heapq.heappush(queue, lines[0][1])
cnt = 1
for i in lines[1:]:
    while queue and queue[0] <= i[0]:
        heapq.heappop(queue)
    heapq.heappush(queue, i[1])
    cnt = max(cnt, len(queue))

print(cnt)