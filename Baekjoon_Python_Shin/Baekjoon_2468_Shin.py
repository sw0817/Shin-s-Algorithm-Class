# 백준 2468 안전 영역
# Baekjoon 2468

# Created by sw0817 on 2021. 01. 28..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2468

# 덱을 활용했다.
from _collections import deque

# BFS 탐색
next = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 현재 위치 r, c를 포함하는 영역을 구한다.
def find(r, c):
    queue = deque()
    queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in next:
            nr = dr + r
            nc = dc + c

            # 방문 여부 없고 현재 설정 높이 i보다 높은 곳을 이어준다.
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and i < arr[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc))


N = int(input())

max_h = 0
result = 1

arr = []

# 입력 값 중 최대 높이를 구한다.
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    if max_h < max(row):
        max_h = max(row)

# 물 높이 0에서 영역은 1개 고정.
# 최대 높이까지 오르면 0개니 그 전까지 탐색
for i in range(1, max_h):

    # 현재 높이에서 영역 수
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):

            # 영역에 해당하는 곳에서 BFS 탐색을 한다.
            if not visited[j][k] and i < arr[j][k]:
                cnt += 1
                visited[j][k] = 1
                find(j, k)

    # 영역 수가 가장 많은 때로 갱신.
    if result < cnt:
        result = cnt

print(result)

