# SWEA 2805 합
# SWEA 2805

# Created by sw0817 on 2020. 12. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE

from _collections import deque

next = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs():
    global result
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((n, n))
    visited[n][n] = 1
    for _ in range(n+1):
        for _ in range(len(queue)):
            r, c = queue.popleft()
            result += farm[r][c]
            for dr, dc in next:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N // 2
    farm = [list(map(int, input())) for _ in range(N)]
    result = 0
    bfs()
    print('#{} {}'.format(tc, result))