# 백준 10845 큐
# Baekjoon 10845

# Created by sw0817 on 2022. 01. 31..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10845

from collections import deque
from sys import stdin

N = int(stdin.readline())
queue = deque()
for _ in range(N):
    command = list(map(str, stdin.readline().split()))
    if 1 < len(command):
        queue.append(command[1])
    else:
        com = command[0]
        if com == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif com == 'size':
            print(len(queue))
        elif com == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif com == 'front':
            if queue:
                n = queue.popleft()
                print(n)
                queue.appendleft(n)
            else:
                print(-1)
        elif com == 'back':
            if queue:
                n = queue.pop()
                print(n)
                queue.append(n)
            else:
                print(-1)