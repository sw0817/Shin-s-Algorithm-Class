# 백준 1113 수영장 만들기
# Baekjoon 1113

# Created by sw0817 on 2021. 02. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1113

# 큐를 사용
from _collections import deque


# 그래프 탐색
next = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())

# 수영장 배열 정보를 가져오면서,
# for 문을 최소화하기 위해 최대 높이 벽을 구한다.
array = []
max_h = 0
for i in range(N):
    row = list(map(int, input()))
    array.append(row)
    for j in range(M):
        if max_h < row[j]:
            max_h = row[j]

# 결과 값
result = 0

# 벽 높이에 따른 채울 수 있는 물 양을 구한다.
for h in range(2, max_h+1):
    visited = [[0] * M for _ in range(N)]
    current = 0
    for i in range(N):
        for j in range(M):

            # 현재 벽 높이보다 낮은 높이라면 채울 수 있다.
            if not visited[i][j] and array[i][j] < h:
                cur = 0
                impossible = False
                queue = deque()
                queue.append((i, j))
                visited[i][j] = 1
                while queue:
                    r, c = queue.popleft()
                    cur += 1

                    # 현재 큐가 바깥과 닿아있다면 물은 다 흘러 넘칠 것이다.
                    if r == 0 or r == N-1 or c == 0 or c == M-1 and not impossible:
                        visited[r][c] = 1
                        impossible = True
                    for dr, dc in next:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and array[nr][nc] < h:
                            visited[nr][nc] = 1
                            queue.append((nr, nc))

                # 흘러 넘친 물은 더하지 않는다.
                if not impossible:
                    current += cur

    result += current

print(result)
