# 백준 2346 풍선 터뜨리기
# Baekjoon 2346

# Created by sw0817 on 2022. 09. 19..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2346

from collections import deque

N = int(input())
queue = deque()
for i, n in enumerate(list(map(int, input().split()))):
    queue.append((i+1, n))

for _ in range(N):
    i, n = queue.popleft()
    print(i, end=' ')

    N -= 1

    if not N:
        break

    if 0 < n:
        n = n % N
        if not n:
            n = N
        for _ in range(n-1):
            queue.append(queue.popleft())
    else:
        n = (n * (-1)) % N
        for _ in range(N - n):
            queue.append(queue.popleft())