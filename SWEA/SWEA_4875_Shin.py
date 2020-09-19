# SWEA 4875 미로
# SWEA 4875

# Created by sw0817 on 2020. 09. 19..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def Maze(i, j):
    visited[i][j] = 1
    if maze[i][j] == 3:
        global cnt
        cnt = 1
        return
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and maze[nr][nc] != 1:
            Maze(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                Maze(i, j)
                break
    print('#{} {}'.format(tc, cnt))
