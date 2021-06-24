# 백준 2146 다리 만들기
# Baekjoon 2146

# Created by sw0817 on 2021. 06. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2146

from _collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def numbering(r, c):
    global n
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    arr[r][c] = n
    while queue:
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc]:
                visited[nr][nc] = 1
                arr[nr][nc] = n
                queue.append((nr, nc))
    n += 1


def explore(r, c):
    global result
    num = arr[r][c]
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    cnt = -1
    while queue:
        cnt += 1
        if result <= cnt:
            break
        con = True
        for _ in range(len(queue)):
            if not con:
                break
            r, c = queue.popleft()
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and not arr[nr][nc] == num:
                    if arr[nr][nc] != 0:
                        if cnt < result:
                            result = cnt
                            con = False
                            break
                    visited[nr][nc] = 1
                    queue.append((nr, nc))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
n = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            numbering(i, j)

result = N * 2
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            explore(i, j)

print(result)

