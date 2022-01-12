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
fires = [0] * (cnt+1)
day = 0
while queue and cnt:
    for _ in range(len(queue)):
        r, c = queue.popleft()
        f = visited[r][c]
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc] == '2':
                if not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = f
                    size += 1
                # 이 외에 다른 불과 만났을 때 합쳐진 불 번호를 비트마스킹 표현할 수 있다.
                # 가장 외곽의 불길을 저장해두어 표현을 바꿔준다.
    day += 1

# print(size, cnt)