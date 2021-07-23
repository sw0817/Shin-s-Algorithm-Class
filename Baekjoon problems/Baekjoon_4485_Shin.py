# 백준 4485 녹색 옷 입은 애가 젤다지?
# Baekjoon 4485

# Created by sw0817 on 2021. 07. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4485

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = 9 * 125 * 125
cnt = 1

while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = INF
    visited = [[INF] * N for _ in range(N)]
    queue = deque()
    queue.append((0, 0, arr[0][0]))
    visited[0][0] = arr[0][0]
    while queue:
        r, c, cur = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and cur + arr[nr][nc] < visited[nr][nc]:
                visited[nr][nc] = cur + arr[nr][nc]
                queue.append((nr, nc, visited[nr][nc]))
                if nr == nc == N-1:
                    result = visited[N-1][N-1]
    print('Problem {}: {}'.format(cnt, result))
    cnt += 1