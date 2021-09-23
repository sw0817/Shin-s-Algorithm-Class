# 백준 2164 카드2
# Baekjoon 2164

# Created by sw0817 on 2021. 09. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])
while 1 < len(queue):
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())