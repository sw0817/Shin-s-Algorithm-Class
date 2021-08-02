# 백준 1938 통나무 옮기기
# Baekjoon 1938

# Created by sw0817 on 2021. 08. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1938

from collections import deque

def rotate(R, C):
    for i in range(R-1, R+2):
        for j in range(C-1, C+2):
            if arr[i][j] == '1':
                return False
    return True


def bfs():
    cnt = -1
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            r, c, v = queue.popleft()
            if r == E[0] and c == E[1] and v == E[2]:
                return cnt
            if v == 0:
                for dr, dc in move:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < N and 1 <= nc < N - 1 and arr[nr][nc - 1] != '1' and arr[nr][nc] != '1' and arr[nr][nc + 1] != '1':
                        if not visited[nr][nc][v]:
                            visited[nr][nc][v] = 1
                            queue.append((nr, nc, v))
            else:
                for dr, dc in move:
                    nr, nc = dr + r, dc + c
                    if nr < 1 or N - 1 <= nr or nc < 0 or N <= nc or arr[nr - 1][nc] == '1' or arr[nr][nc] == '1' or arr[nr + 1][nc] == '1':
                        continue
                    if not visited[nr][nc][v]:
                        visited[nr][nc][v] = 1
                        queue.append((nr, nc, v))

            if 1 <= r < N - 1 and 1 <= c < N - 1 and rotate(r, c):
                v = 1 if v == 0 else 0
                if not visited[r][c][v]:
                    visited[r][c][v] = 1
                    queue.append((r, c, v))
    return 0


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
arr = []
start = []
end = []
for i in range(N):
    row = list(input())
    for j in range(N):
        if row[j] == 'B':
            start.append((i, j))
        elif row[j] == 'E':
            end.append((i, j))
    arr.append(row)

visited = [[[0] * 2 for _ in range(N)] for _ in range(N)]

queue = deque()

sr, sc = start[1]
if start[0][0] == start[1][0]:
    visited[sr][sc][0] = 0
    queue.append((sr, sc, 0))
else:
    visited[sr][sc][1] = 0
    queue.append((sr, sc, 1))

er, ec = end[1]
if end[0][0] == end[1][0]:
    E = (er, ec, 0)
else:
    E = (er, ec, 1)

print(bfs())