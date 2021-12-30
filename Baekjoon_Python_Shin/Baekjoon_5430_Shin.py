# 백준 5430 AC
# Baekjoon 5430

# Created by sw0817 on 2021. 12. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5430

from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    info = input()
    if n < p.count('D'):
        print('error')
        continue
    queue = deque()
    arr = list(map(int, info[1:-1].split(','))) if n else []
    for i in arr:
        queue.append(i)
    rev = False
    for f in p:
        if f == 'D':
            if rev:
                queue.pop()
            else:
                queue.popleft()
        else:
            if rev:
                rev = False
            else:
                rev = True

    ret = '['
    if rev:
        while queue:
            ret += str(queue.pop()) + ','
    else:
        while queue:
            ret += str(queue.popleft()) + ','

    ret = ret[:-1] + ']'
    print('[]' if len(ret) == 1 else ret)