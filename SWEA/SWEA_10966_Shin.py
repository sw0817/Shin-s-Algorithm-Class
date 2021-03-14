# SWEA 10966 물놀이를 가자
# SWEA 10966

# Created by sw0817 on 2021. 03. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST&categoryId=AXWXMZta-PsDFAST&categoryType=CODE&problemTitle=%EB%AC%BC%EB%86%80%EC%9D%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    visited = [[-1] * N for _ in range(M)]
    queue = deque()
    for i in range(M):
        row = input()
        for j in range(N):
            if row[j] == 'W':
                visited[i][j] = 0
                queue.append((i, j))

    ans = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

    for row in visited:
        ans += sum(row)

    print('#{} {}'.format(tc, ans))