# 백준 1584 게임
# Baekjoon 1584

# Created by sw0817 on 2021. 11. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1584

import math
from collections import deque

def setArr(n, p):
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                arr[i][j] = p


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arr = [[0] * 501 for _ in range(501)]
visited = [[math.inf] * 501 for _ in range(501)]
visited[0][0] = 0

setArr(int(input()), 1)
setArr(int(input()), 2)

queue = deque()
queue.append((0, 0))
while queue:
    r, c = queue.popleft()
    if r == 500 and c == 500:
        break
    cur = visited[r][c]
    for dr, dc in move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 501 and 0 <= nc < 501:
            if arr[nr][nc] == 0 and cur < visited[nr][nc]:
                visited[nr][nc] = cur
                queue.append((nr, nc))
            elif arr[nr][nc] == 1 and cur + 1 < visited[nr][nc]:
                visited[nr][nc] = cur + 1
                queue.append((nr, nc))

print(-1 if visited[500][500] == math.inf else visited[500][500])