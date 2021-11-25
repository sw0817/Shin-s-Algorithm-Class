# 백준 2536 버스 갈아타기
# Baekjoon 2536

# Created by sw0817 on 2021. 11. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2536

from collections import deque

def bus_con(x1, x2, y1, y2, c1, c2, r1, r2):
    if x1 == c1:
        if y1 <= r1 <= y2 or y1 <= r2 <= y2 or r1 <= y1 <= r2 or r1 <= y2 <= r2:
            return True
    if x2 == c2:
        if y1 <= r1 <= y2 or y1 <= r2 <= y2 or r1 <= y1 <= r2 or r1 <= y2 <= r2:
            return True
    if y1 == r1:
        if x1 <= c1 <= x2 or x1 <= c2 <= x2 or c1 <= x1 <= c2 or c1 <= x2 <= c2:
            return True
    if y2 == r2:
        if x1 <= c1 <= x2 or x1 <= c2 <= x2 or c1 <= x1 <= c2 or c1 <= x2 <= c2:
            return True
    if x1 <= c1 <= x2 and y1 <= r1 <= y2 or c1 <= x1 <= c2 and r1 <= y1 <= r2:
        return True
    if x1 <= c1 <= x2 and r1 <= y1 <= r2 or c1 <= x1 <= c2 and y1 <= r1 <= y2:
        return True
    return False


def bfs():
    cnt = 1
    visited = [0] * (k+1)
    for b in queue:
        visited[b] = 1
    while queue:
        for _ in range(len(queue)):
            b = queue.popleft()
            if b in final_set:
                return cnt
            for n_b in adj[b]:
                if not visited[n_b]:
                    queue.append(n_b)
                    visited[n_b] = 1
        cnt += 1


m, n = map(int, input().split())
k = int(input())

adj = [[] for _ in range(k+1)]
info = []
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    info.append([x1, y1, x2, y2, b])

queue = deque()
final_set = set()
sx, sy, dx, dy = map(int, input().split())

for i in range(k-1):
    x1, y1, x2, y2, b = info[i]
    if x1 <= sx <= x2 and y1 == sy or x1 <= sx <= x2 and y2 == sy or y1 <= sy <= y2 and x1 == sx or y1 <= sy <= y2 and x2 == sx:
        queue.append(b)
    if x1 <= dx <= x2 and y1 == dy or x1 <= dx <= x2 and y2 == dy or y1 <= dy <= y2 and x1 == dx or y1 <= dy <= y2 and x2 == dx:
        final_set.add(b)
    for j in range(i+1, k):
        c1, r1, c2, r2, b2 = info[j]
        if bus_con(x1, x2, y1, y2, c1, c2, r1, r2):
            adj[b].append(b2)
            adj[b2].append(b)

x1, y1, x2, y2, b = info[k-1]
if x1 <= sx <= x2 and y1 == sy or x1 <= sx <= x2 and y2 == sy or y1 <= sy <= y2 and x1 == sx or y1 <= sy <= y2 and x2 == sx:
    queue.append(b)
if x1 <= dx <= x2 and y1 == dy or x1 <= dx <= x2 and y2 == dy or y1 <= dy <= y2 and x1 == dx or y1 <= dy <= y2 and x2 == dx:
    final_set.add(b)

print(bfs())