# 백준 5213 과외맨
# Baekjoon 5213

# Created by sw0817 on 2021. 07. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5213

## 인접리스트로 바꿔보자
from collections import deque

lr = [(0, 1), (0, -1)]
ud = [(1, 0), (-1, 0)]
lud = [(1, -1), (-1, -1)]
rud = [(1, 1), (-1, 1)]
move = lr + ud + lud + rud

N = int(input())
arr = []
for i in range(N):
    row = []
    if i % 2:
        row.append((0, 0))
        for _ in range(N-1):
            row.append(tuple(map(int, (input()).split())))
        row.append((0, 0))
    else:
        for _ in range(N):
            row.append(tuple(map(int, (input()).split())))
        row.append((0, 0))
    arr.append(row)

# for row in arr:
#     print(row)

visited = [[0] * (N+1) for _ in range(N+1)]

queue = deque()
queue.append((0, 0, "1 "))
visited[0][0] = 1
result = []
while queue:
    # print(queue)
    r, c, l = queue.popleft()
    a, b = arr[r][c]
    result.append(l)
    for i in range(8):
        dr, dc = move[i]
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N+1 and not visited[nr][nc] and arr[nr][nc][0]:
            if nr % 2:
                dl = str(nr * N + nc)
            else:
                dl = str(nr * N + nc + 1 - (nr // 2))
            if i < 2:
                visited[nr][nc] = 1
                queue.append((nr, nc, l+dl+" "))
            elif i < 4:
                if b == arr[nr][nc][0]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, l+dl+" "))
            elif i < 6:
                if not r % 2:
                    continue
                if a == arr[nr][nc][1]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, l + dl+" "))
            elif i < 8:
                if r % 2:
                    continue
                if b == arr[nr][nc][0]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc, l+dl+" "))

result.sort(key=lambda x : list(map(int, x.split()))[-1])
print(*list(result[-1].split()))