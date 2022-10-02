# 백준 2234 성곽
# Baekjoon 2234

# Created by sw0817 on 2022. 10. 02..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2234

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
visited = [[0] * N for _ in range(M)]
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = [0]
num = 1
max_cnt = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            cur = 0
            visited[i][j] = num
            queue = deque()
            queue.append((i, j))
            while queue:
                r, c = queue.popleft()
                cur += 1
                info = arr[r][c]
                for k in range(3, -1, -1):
                    if 2 ** k <= info:
                        info -= 2 ** k
                    else:
                        dr, dc = move[3-k]
                        nr, nc = r + dr, c + dc
                        if not visited[nr][nc]:
                            visited[nr][nc] = num
                            queue.append((nr, nc))

            cnt.append(cur)
            num += 1

for i in range(M):
    for j in range(N):
        if visited[i][j]:
            cur = visited[i][j]
            queue = deque()
            queue.append((i, j))
            while queue:
                r, c = queue.popleft()
                visited[r][c] = 0
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N:
                        if visited[nr][nc] == cur:
                            queue.append((nr, nc))
                        elif visited[nr][nc]:
                            max_cnt = max(max_cnt, cnt[cur] + cnt[visited[nr][nc]])

print(num - 1)
print(max(cnt))
print(max_cnt)

# 메모리 시간 초과