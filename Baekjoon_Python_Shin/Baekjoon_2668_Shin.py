# 백준 2668 숫자고르기
# Baekjoon 2668

# Created by sw0817 on 2021. 11. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2668

N = int(input())
cnt = 0
visited = [0] * (N+1)
info = []
for i in range(1, N+1):
    n = int(input())
    info.append(n)
    if n == i:
        visited[i] = 1

for i in range(1, N+1):
    if not visited[i]:
        queue = []
        queue.append(i)
        nxt = info[i-1]
        while not nxt in queue and not visited[nxt]:
            queue.append(nxt)
            nxt = info[nxt-1]

        idx = 0
        while idx < len(queue) and queue[idx] != nxt:
            idx += 1
        while idx < len(queue):
            visited[queue[idx]] = 1
            idx += 1

print(sum(visited))
for i in range(1, N+1):
    if visited[i]:
        print(i)