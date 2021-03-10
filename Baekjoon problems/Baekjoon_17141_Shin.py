# 백준 17141 연구소2
# Baekjoon 17141

# Created by sw0817 on 2021. 03. 10..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17141

from itertools import combinations
from _collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())

arr = []

# virus 시작 가능 위치
virus = []

# 벽 위치
wall = []

# 바이러스가 퍼질 수 없으면 -1
result = -1

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 1:
            wall.append((i, j))
    arr.append(row)

# 가능한 모든 바이러스 시작 위치 조합에 대해
for comb in combinations(virus, M):

    # 바이러스가 퍼지지 않은 곳은 -1
    visited = [[-1] * N for _ in range(N)]

    # 벽은 0으로 세팅해준다.
    for r, c in wall:
        visited[r][c] = 0

    # 시작 위치들을 큐에 넣고, 그 자리들은 0
    queue = deque(comb)
    for r, c in comb:
        visited[r][c] = 0

    # 소요 시간
    cnt = 0

    while queue:

        # 현재 큐에서 모두 퍼지면 1초 증가
        cnt += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if arr[nr][nc] == 0 or arr[nr][nc] == 2:
                        if visited[nr][nc] == -1 or cnt < visited[nr][nc]:
                            visited[nr][nc] = cnt
                            queue.append((nr, nc))

    current = -1
    check = True
    for i in range(N):

        # 안 퍼진 곳이 있으면 무효
        if -1 in visited[i]:
            check = False
            break

        # 가장 오래 걸린 시간을 찾는다.
        else:
            current = max(current, max(visited[i]))

    if check:
        if result == -1:
            result = current
        elif current < result:
            result = current

print(result)