# SWEA 1226 미로1
# SWEA 1226

# Created by sw0817 on 2020. 09. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE


def Maze(i, j):
    visited[i][j] = 1
    if maze[i][j] == 3:
        global cnt
        cnt = 1
        return
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < 16 and 0 <= nc < 16 and visited[nr][nc] == 0 and maze[nr][nc] != 1:
            Maze(nr, nc)


for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    visited = [([0] * 16) for _ in range(16)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    cnt = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                Maze(i, j)
                break
    print('#{} {}'.format(tc, cnt))
