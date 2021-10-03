# 백준 1726 로봇
# Baekjoon 1726

# Created by sw0817 on 2021. 02. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1726

from collections import deque

# 동서남북 1 ~ 4 에 맞게 index 설정
next = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

M, N = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(M)]

# 초기 행, 열, 방향(1,2,3,4 동서남북)
# 입력 좌표는 0부터가 아닌 1부터이다.
ir, ic, id = map(int, input().split())
ir -= 1
ic -= 1

# 목표
# 입력 좌표는 0부터가 아닌 1부터이다.
fr, fc, fd = map(int, input().split())
fr -= 1
fc -= 1

# 방향별 방문배열 (동서남북 방향 순)
visited = [[[-1] * N for _ in range(M)] for _ in range(4)]

queue = deque()
queue.append((ir, ic, id, 0))

# 현재 방향, 위치에서 0
visited[id-1][ir][ic] = 0

while queue:
    r, c, d, cnt = queue.popleft()

    # 직진은 현재 방향으로만.
    dr, dc = next[d]

    # 1칸 ~ 3칸 갈 수 있고, 중간에 벽이 있다면 멈춘다.
    for i in range(1, 4):
        nr, nc = r + dr * i, c + dc * i

        # 배열 내 통로라면
        if 0 <= nr < M and 0 <= nc < N and array[nr][nc] == 0:

            # 이 방향으로 방문한적이 없거나, 기존 방법보다 짧게 왔을 시 갱신
            if visited[d-1][nr][nc] == -1 or cnt + 1 < visited[d-1][nr][nc]:
                visited[d-1][nr][nc] = cnt + 1
                queue.append((nr, nc, d, cnt+1))

        # 벽이면 멈춘다.
        else:
            break

    # 동서 방향에선 남북 방향으로 명령 1회
    if d < 3:
        for i in range(3, 5):
            if cnt + 1 < visited[i-1][r][c] or visited[i-1][r][c] == -1:
                visited[i-1][r][c] = cnt + 1
                queue.append((r, c, i, cnt+1))

    # 남북 방향에선 동북 방향으로 명령 1회
    else:
        for i in range(1, 3):
            if cnt + 1 < visited[i-1][r][c] or visited[i-1][r][c] == -1:
                visited[i-1][r][c] = cnt + 1
                queue.append((r, c, i, cnt+1))

# 타겟 위치, 방향 명령 최소횟수 출력
print(visited[fd-1][fr][fc])