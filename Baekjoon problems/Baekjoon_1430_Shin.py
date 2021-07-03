# 백준 1430 공격
# Baekjoon 1430

# Created by sw0817 on 2021. 07. 02..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1430

from collections import deque

N, R, D, X, Y = map(int, input().split())

# tops = deque()
# for _ in range(N):
#     x, y = map(int, input().split())
#     tops.append((x, y))
#
# result = 0
#
# mag = 1
# temp = deque()
# temp.append((X, Y))
# while tops:
#     remain = deque()
#     temp2 = deque()
#     for _ in range(len(tops)):
#         x, y = tops.popleft()
#         energy = False
#         for X, Y in temp:
#             if (abs(X-x) ** 2 + abs(Y-y) ** 2) ** 0.5 <= R:
#                 temp2.append((x, y))
#                 result += D * mag
#                 energy = True
#                 break
#         if not energy:
#             remain.append((x, y))
#
#     tops = remain
#     temp = temp2
#     mag /= 2
#
# print(round(result, 3))

###########

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

arr = [[0] * 1001 for _ in range(1001)]
for _ in range(N):
    x, y = map(int, input().split())
    arr[x][y] = 1

result = 0
mag = 1
queue = deque()
queue.append((X, Y))
while queue:
    for _ in range(len(queue)):
        visited = [[0] * 1001 for _ in range(1001)]
        x, y = queue.popleft()
        visited[x][y] = 1
        queue2 = deque()
        queue2.append((x, y))
        while queue2:
            x2, y2 = queue2.popleft()
            for dx, dy in move:
                nx, ny = x2 + dx, y2 + dy
                if nx < 0 or 1000 < nx or ny < 0 or 1000 < ny:
                    continue
                if (abs(nx-x) ** 2 + abs(ny-y) ** 2) ** 0.5 <= R and not visited[nx][ny]:
                    if arr[nx][ny] == 1:
                        arr[nx][ny] = 2
                        result += D * mag
                        queue.append((nx, ny))
                    queue2.append((nx, ny))
                    visited[nx][ny] = 1
    mag /= 2

print(round(result, 3))
