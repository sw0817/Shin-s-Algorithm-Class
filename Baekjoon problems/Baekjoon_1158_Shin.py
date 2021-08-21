# 백준 1158 요세푸스 문제
# Baekjoon 1158

# Created by sw0817 on 2021. 08. 21..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1158

from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
print("<", end="")
cnt = 1
while queue:
    n = queue.popleft()
    if cnt == K:
        print(n, end="")
        if queue:
            print(",", end=" ")
        cnt = 1
    else:
        queue.append(n)
        cnt += 1
print(">")