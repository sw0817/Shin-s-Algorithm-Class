# 백준 1595 북쪽나라의 도로
# Baekjoon 1595

# Created by sw0817 on 2021. 03. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1595

from _collections import deque

def check(b, l, c):
    visited[b] = 1
    for r, nl in adj[b]:
        if not visited[r]:
            check(r, nl, c + l)
    if max_visited[b] < c+l:
        max_visited[b] = c+l
    visited[b] = 0


adj = [[] for _ in range(10001)]
visited = [0] * 10001
max_visited = [0] * 10001

a = 1
while a:
    try:
        A, B, L = map(int, input().split())
        is_input = 1
        adj[A].append((B, L))
        adj[B].append((A, L))

    except EOFError:
        a = 0

queue = deque(adj[A])
visited[A] = 1

while queue:
    b, l = queue.popleft()
    check(b, l, 0)

n = max(max_visited)
idx = max_visited.index(n)

visited = [0] * 10001
visited[idx] = 1
for b, l in adj[idx]:
    check(b, l, 0)

print(max(max_visited))

