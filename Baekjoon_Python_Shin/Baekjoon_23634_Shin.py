# 백준 23634 미안하다 이거 보여주려고 어그로 끌었다
# Baekjoon 23634

# Created by sw0817 on 2022. 01. 12..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/23634

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def findFire():
    global cnt, size
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0' and not visited[i][j]:
                cnt += 1
                size += makeFire(cnt, i, j)


def makeFire(n, r, c):
    curQueue = deque()
    curQueue.append((r, c))
    queue.append((r, c))
    visited[r][c] = n
    num = 1
    while curQueue:
        r, c = curQueue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == '0':
                visited[nr][nc] = n
                curQueue.append((nr, nc))
                queue.append((nr, nc))
                num += 1

    return num


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
size = 0
cnt = 0
visited = [[0] * M for _ in range(N)]
queue = deque()
findFire()
# for row in visited:
#     print(row)
fires = [set() for _ in range(cnt+1)]
day = 0
result = [0, size]
while queue:
    meet = False
    for _ in range(len(queue)):
        r, c = queue.popleft()
        f = visited[r][c]
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc] == '2' and not visited[nr][nc] == f:
                if not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = f
                    size += 1
                    for dr2, dc2 in move:
                        nnr, nnc = nr + dr2, nc + dc2
                        if 0 <= nnr < N and 0 <= nnc < M and not arr[nnr][nnc] == '2':
                            num = visited[nnr][nnc]
                            if not num:
                                continue
                            if not num == f and not num in fires[f]:
                                fires[num].add(f)
                                fires[f].add(num)
                                for vf in fires[f]:
                                    fires[vf] |= fires[num]
                                    fires[vf].discard(vf)
                                    if num != vf:
                                        fires[num].add(vf)
                                for vf in fires[f]:
                                    fires[vf] |= fires[num]
                                    fires[vf].discard(vf)
                                    if num != vf:
                                        fires[num].add(vf)
                                meet = True
                # else:
                #     cf = visited[nr][nc]
                #     if not cf in fires[f]:
                #         for vf in fires[f]:
                #             fires[vf].add(cf)
                #             fires[cf].add(vf)
                #         fires[cf].add(f)
                #         fires[f].add(cf)
                #         meet = True

    day += 1
    # print(day)
    # for row in visited:
    #     print(row)
    # print(fires)
    # print()
    if meet:
        result = [day, size]

print(*result)
print(fires)
# for row in visited:
#     print(row)
# print()