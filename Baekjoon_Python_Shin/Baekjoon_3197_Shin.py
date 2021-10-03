# 백준 3197 백조의 호수
# Baekjoon 3197

# Created by sw0817 on 2021. 04. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3197

from _collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    while queue:
        r, c = queue.popleft()
        if r == r2 and c == c2:
            return 1
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if not b[nr][nc]:
                    if arr[nr][nc] == '.':
                        queue.append([nr, nc])
                    else:
                        temp_queue.append([nr, nc])
                    b[nr][nc] = 1
    return 0


def melt():
    while wQueue:
        r, c = wQueue.popleft()
        if arr[r][c] == 'X':
            arr[r][c] = '.'

        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if not wb[nr][nc]:
                    if arr[nr][nc] == 'X':
                        temp_wQueue.append([nr, nc])
                    else:
                        wQueue.append([nr, nc])
                    wb[nr][nc] = 1


R, C = map(int, input().split())
b = [[0] * C for _ in range(R)]
wb = [[0] * C for _ in range(R)]

arr = []
swan = []

queue = deque()
temp_queue = deque()
wQueue = deque()
temp_wQueue = deque()

for i in range(R):
    row = list(input())
    arr.append(row)
    for j in range(C):
        if row[j] == 'L':
            swan.extend([i, j])
            wQueue.append([i, j])
        elif row[j] == '.':
            wb[i][j] = 1
            wQueue.append([i, j])

r1, c1, r2, c2 = swan

queue.append([r1, c1])
arr[r1][c1], arr[r2][c2], b[r1][c1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    queue, wQueue = temp_queue, temp_wQueue
    temp_queue, temp_wQueue = deque(), deque()
    cnt += 1