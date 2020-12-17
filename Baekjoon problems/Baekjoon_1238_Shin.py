# 백준 1238 파티
# Baekjoon 1238

# Created by sw0817 on 2020. 12. 18..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1238

from _collections import deque


def getX(idx):
    visited = [100 * 2000] * N
    queue = deque()
    for info in adj[idx]:
        visited[info[0]] = info[1]
        queue.append(info[0])

    while queue:
        i = queue.popleft()
        for info in adj[i]:
            if visited[info[0]] > visited[i] + info[1]:
                visited[info[0]] = visited[i] + info[1]
                queue.append(info[0])

    students[X-1] = visited[X-1]


def get(idx):
    visited = [100*2000] * N
    visited[idx] = 0
    queue = deque()
    queue.append(idx)
    while queue:
        i = queue.popleft()
        for info in adj[i]:
            if visited[info[0]] > visited[i] + info[1]:
                visited[info[0]] = visited[i] + info[1]
                queue.append(info[0])

    go = visited[X-1]
    visited = [100*2000] * N
    visited[X-1] = 0
    queue = deque()
    queue.append(X-1)
    while queue:
        i = queue.popleft()
        for info in adj[i]:
            if visited[info[0]] > visited[i] + info[1]:
                visited[info[0]] = visited[i] + info[1]
                queue.append(info[0])

    back = visited[idx]

    students[idx] = go + back




N, M, X = map(int, input().split())

adj = [[] for _ in range(N)]

for _ in range(M):
    start, end, t = map(int, input().split())
    adj[start-1].append([end-1, t])

# print(adj)

students = [100*2000] * N

for i in range(N):
    if i == X-1:
        getX(i)
    else:
        get(i)

# print(students)

print(max(students))
