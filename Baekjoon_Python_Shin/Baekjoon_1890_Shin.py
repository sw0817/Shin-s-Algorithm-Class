# 백준 1890 점프
# Baekjoon 1890

# Created by sw0817 on 2022. 11. 13..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1890

import heapq

move = [(1, 0), (0, 1)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = []
heapq.heappush(queue, (0, 0))
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
while queue:
    r, c = heapq.heappop(queue)
    if r == N-1 and c == N-1:
        break
    n = dp[r][c]
    d = arr[r][c]

    for dr, dc in move:
        nr, nc = r + dr * d, c + dc * d
        if 0 <= nr < N and 0 <= nc < N:
            dp[nr][nc] += n
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                heapq.heappush(queue, (nr, nc))

print(dp[-1][-1])