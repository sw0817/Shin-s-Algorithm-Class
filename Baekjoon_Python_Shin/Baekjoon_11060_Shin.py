# 백준 11060 점프 점프
# Baekjoon 11060

# Created by sw0817 on 2022. 01. 04..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11060

import math
from collections import deque

N = int(input())
As = list(map(int, input().split()))
visited = [math.inf] * N
visited[0] = 0
queue = deque()
queue.append((0, 0))
while queue:
    cnt, idx = queue.popleft()
    for i in range(1, As[idx]+1):
        if idx + i < N and cnt + 1 < visited[idx+i]:
            visited[idx+i] = cnt + 1
            queue.append((cnt+1, idx+i))

print(-1 if visited[N-1] == math.inf else visited[N-1])