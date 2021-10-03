# 백준 1697 숨바꼭질
# Baekjoon 1697

# Created by sw0817 on 2020. 12. 15..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1697

from _collections import deque


def go(i):
    t = 0
    queue = deque([[i, t]])
    while queue:
        i = queue.popleft()
        e = i[0]
        t = i[1]
        if not visited[e]:
            visited[e] = True
            if e == K:
                return t
            t += 1
            if e*2 <= 100000:
                queue.append([e*2, t])
            if e+1 <= 100000:
                queue.append([e+1, t])
            if 0 <= e-1:
                queue.append([e-1, t])
    return t


N, K = map(int, input().split())
visited = [False] * 1000001

if N == K:
    print(0)
else:
    print(go(N))

