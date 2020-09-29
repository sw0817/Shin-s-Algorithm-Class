# SWEA 5105 미로의 거리
# SWEA 5105

# Created by sw0817 on 2020. 09. 29..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(i, j, sum):
    global result
    if maze[i][j] == 3:
        result = sum
        return
    visited[i][j] = 1
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if nr < 0 or N <= nr or nc < 0 or N <= nc or visited[nr][nc] == 1 or maze[nr][nc] == 1:
            continue
        else:
            bfs(nr, nc, sum + 1)


T = int(input())
for tc in range(1, T+1):
    result = 1
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                bfs(i, j, 0)
                print('#{} {}'.format(tc, result-1))
                break
