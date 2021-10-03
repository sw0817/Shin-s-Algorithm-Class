# 백준 10828 스택
# Baekjoon 10828

# Created by sw0817 on 2021. 05. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10828

from collections import deque
from sys import stdin

N = int(stdin.readline())
stack = deque()
l = 0

for _ in range(N):
    info = stdin.readline().split()
    if info[0] == 'top':
        if l == 0:
            print(-1)
        else:
            print(stack[-1])
    elif info[0] == 'size':
        print(l)
    elif info[0] == 'empty':
        if l == 0:
            print(1)
        else:
            print(0)
    elif info[0] == 'pop':
        if l == 0:
            print(-1)
        else:
            l -= 1
            print(stack.pop())
    else:
        top = info[1]
        stack.append(top)
        l += 1