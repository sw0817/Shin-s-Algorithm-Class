# SWEA 10914 상훈이의 런닝메이즈
# SWEA 10914

# Created by sw0817 on 2021. 03. 22..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXVJJtuKKi8DFASe

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def check(i, j, time, lv, star):
    global result2
    if map_[i][j] == 6:
        point = lv * (star + time)
        if point > result2:
            result2 = point
        return
    if time <= 0:
        return

    visited[i][j] = 1
    for k in range(4):
        nr = dr[k] + i
        nc = dc[k] + j
        if nr < 0 or N <= nr or nc < 0 or N <= nc:
            continue
        else:
            if map_[nr][nc] == 4:
                temp = 3
                nr = dr[k] * temp + i
                nc = dc[k] * temp + j
                while 0 <= nr < N and 0 <= nc < N:
                    if map_[nr][nc] == 4:
                        temp += 2
                        nr = dr[k] * temp + i
                        nc = dc[k] * temp + j
                        continue
                    break
                if nr < 0 or N <= nr or nc < 0 or N <= nc:
                    continue

            if map_[nr][nc] == 1 or visited[nr][nc]:
                continue
            elif map_[nr][nc] == 2:
                check(nr, nc, time + 4, lv, star)
            elif map_[nr][nc] == 3:
                check(nr, nc, time - 6, lv + 1, star)
            elif map_[nr][nc] == 7:
                check(nr, nc, time - 1, lv, star + 1)
            else:
                check(nr, nc, time - 1, lv, star)
    visited[i][j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    map_ = []
    result2 = -1
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 5:
                start = (i, j)
        map_.append(row)

    check(start[0], start[1], 10, 1, 0)
    print('#{} {}'.format(tc, result2))