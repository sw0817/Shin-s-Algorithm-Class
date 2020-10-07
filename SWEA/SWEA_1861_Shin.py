# SWEA 1861 정사각형 방
# SWEA 1861

# Created by sw0817 on 2020. 10. 07..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc&categoryId=AV5LtJYKDzsDFAXc&categoryType=CODE


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def room(i, j, cnt):
    global result, final_room
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if nr < 0 or N <= nr or nc < 0 or N <= nc:
            continue
        if rooms[nr][nc] == rooms[i][j] + 1:
            room(nr, nc, cnt+1)
            return
    if cnt > result:
        result = cnt
        final_room = rooms[i][j] - cnt + 1
    elif cnt == result:
        if rooms[i][j] - cnt + 1 < final_room:
            final_room = rooms[i][j] - cnt + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    final_room = N ** 2 + 1
    for i in range(N):
        for j in range(N):
            if (N ** 2) - rooms[i][j] + 1 < result or final_room < rooms[i][j] < final_room + result:
                continue
            room(i, j, 1)

    print('#{} {} {}'.format(tc, final_room, result))