# 백준 5213 과외맨
# Baekjoon 5213

# Created by sw0817 on 2021. 07. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5213

## 인접리스트로 바꿔보자

from collections import deque

N = int(input())
num = N ** 2 - N // 2 + 1
info = [(0, 0)]
adj = [[] for _ in range(num)]
for i in range(1, N+1):
    info.append(tuple(input().split()))
    if 1 < i and info[i][0] == info[i-1][1]:
        adj[i].append(i-1)
        adj[i-1].append(i)

cnt = N
for i in range(N-1):
    if not i % 2:
        for j in range(N-1):
            cnt += 1
            a, b = input().split()
            info.append((a, b))

            if 0 < j and info[cnt][0] == info[cnt-1][1]:
                adj[cnt].append(cnt-1)
                adj[cnt-1].append(cnt)

            if info[cnt-N][1] == a:
                adj[cnt-N].append(cnt)
                adj[cnt].append(cnt-N)
            if info[cnt+1-N][0] == b:
                adj[cnt+1-N].append(cnt)
                adj[cnt].append(cnt+1-N)

    else:
        for j in range(N):
            cnt += 1
            a, b = input().split()
            info.append((a, b))

            if 0 < j and info[cnt][0] == info[cnt-1][1]:
                adj[cnt].append(cnt-1)
                adj[cnt-1].append(cnt)

            if j < N-1 and info[cnt+1-N][0] == b:
                adj[cnt+1-N].append(cnt)
                adj[cnt].append(cnt+1-N)
            if j != 0 and info[cnt-N][1] == a:
                adj[cnt - N].append(cnt)
                adj[cnt].append(cnt - N)

queue = deque()
queue.append(1)
visited = [0] * num
visited[1] = 1
result = 1
path = [0] * num
while queue:
    n = queue.popleft()
    for v in adj[n]:
        if not visited[v]:
            visited[v] = 1
            result = max(result, v)
            path[v] = n
            queue.append(v)

p = [result]
x = result
# print(result)
while path[x]:
    x = path[x]
    p.append(x)

p.reverse()
print(str(len(p)))
# print(' '.join(map(str, p)))
print(*p)
# print(path)
print(adj)


##########
# from collections import deque
#
# lr = [(0, 1), (0, -1)]
# ud = [(1, 0), (-1, 0)]
# lud = [(1, -1), (-1, -1)]
# rud = [(1, 1), (-1, 1)]
# move = lr + ud + lud + rud
#
# N = int(input())
# arr = []
# for i in range(N):
#     row = []
#     if i % 2:
#         row.append((0, 0))
#         for _ in range(N-1):
#             row.append(tuple(map(int, (input()).split())))
#         row.append((0, 0))
#     else:
#         for _ in range(N):
#             row.append(tuple(map(int, (input()).split())))
#         row.append((0, 0))
#     arr.append(row)
#
# # for row in arr:
# #     print(row)
#
# visited = [[0] * (N+1) for _ in range(N+1)]
#
# queue = deque()
# queue.append((0, 0, "1 "))
# visited[0][0] = 1
# result = []
# while queue:
#     # print(queue)
#     r, c, l = queue.popleft()
#     a, b = arr[r][c]
#     result.append(l)
#     for i in range(8):
#         dr, dc = move[i]
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < N and 0 <= nc < N+1 and not visited[nr][nc] and arr[nr][nc][0]:
#             if nr % 2:
#                 dl = str(nr * N + nc)
#             else:
#                 dl = str(nr * N + nc + 1 - (nr // 2))
#             if i < 2:
#                 visited[nr][nc] = 1
#                 queue.append((nr, nc, l+dl+" "))
#             elif i < 4:
#                 if b == arr[nr][nc][0]:
#                     visited[nr][nc] = 1
#                     queue.append((nr, nc, l+dl+" "))
#             elif i < 6:
#                 if not r % 2:
#                     continue
#                 if a == arr[nr][nc][1]:
#                     visited[nr][nc] = 1
#                     queue.append((nr, nc, l + dl+" "))
#             elif i < 8:
#                 if r % 2:
#                     continue
#                 if b == arr[nr][nc][0]:
#                     visited[nr][nc] = 1
#                     queue.append((nr, nc, l+dl+" "))
#
# result.sort(key=lambda x : list(map(int, x.split()))[-1])
# print(*list(result[-1].split()))