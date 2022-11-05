# 백준 1021 회전하는 큐
# Baekjoon 1021

# Created by sw0817 on 2022. 11. 05..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1021

from collections import deque

N, M = map(int, input().split())
pos = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])

cnt = 0
for i in pos:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1

print(cnt)