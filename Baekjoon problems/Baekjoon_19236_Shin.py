# 백준 19236 청소년 상어
# Baekjoon 19236

# Created by sw0817 on 2021. 03. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/19236

from copy import deepcopy

# 상어가 물고기를 먹는 방법이 최대 3개이므로 재귀 & deepcopy
def eat_fish(array, r, c, cnt):
    global result
    array = deepcopy(array)

    # 현재 상어위치 물고기 번호
    fish = array[r][c][0]

    # 먹으면 번호 0으로 초기화
    array[r][c][0] = 0

    # 모든 물고기 위치 확인
    for i in range(1, 17):
        x, y = -1, -1
        flag = False
        for j in range(4):
            if flag:
                break
            for k in range(4):
                if array[j][k][0] == i:
                    x, y = j, k
                    flag = True
                    break

        # 이미 먹힌 물고기면 다음 물고기
        if x == -1 and y == -1:
            continue

        # 해당 물고기 현재 움직임 방향
        dir = array[x][y][1]

        # 현재 위치부터 반시계로 8방향 돌면서 움직일 수 있는지 확인
        for _ in range(8):
            dx, dy = dirs[dir]
            nx, ny = x + dx, y + dy

            # 배열 안에서 상어 위치가 아니라면 움직인다.
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (r, c):
                array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                array[x][y][1], array[nx][ny][1] = array[nx][ny][1], dir
                break

            dir = (dir + 1) % 8

    # 상어가 갈 수 있는 위치 배열
    shark_stack = []

    # 상어 움직임 방향
    dir = array[r][c][1]
    dr, dc = dirs[dir]

    # 최대 3칸 움직일 수 있음
    for i in range(1, 4):
        nr, nc = r + dr * i, c + dc * i

        # 배열 안이고 물고기 있으면 갈 수 있음
        if 0 <= nr < 4 and 0 <= nc < 4 and 1 <= array[nr][nc][0] <= 16:
            shark_stack.append((nr, nc))

    # 최종 값은 큰 값
    result = max(result, cnt + fish)

    # 갈 수 있는 방향으로 가서 그 배열을 사용해 재귀
    for nr, nc in shark_stack:
        eat_fish(array, nr, nc, cnt+fish)


# 위쪽부터 반시계 방향
dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
arr = [[0] * 4 for _ in range(4)]
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(0, 8, 2):
        num, dir = info[j], info[j+1]

        # arr에 물고기 번호, 방향으로 표시
        # 방향 index 0부터 쓰기위해 -1
        arr[i][j // 2] = [num, dir-1]

result = 0

# 0, 0 부터 먹는다.
eat_fish(arr, 0, 0, 0)

print(result)