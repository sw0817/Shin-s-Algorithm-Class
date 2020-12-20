# 백준 1938 게임 개발
# Baekjoon 1938

# Created by sw0817 on 2020. 12. 21..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1938

# 상태
# 통나무 가로 = 2 세로 = 3
# 최종 가로 = 4 세로 = 5

next = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def move(r, c, cnt, type):
    global result

    for visit in visited:
        print(visit)
    print()
    for visit2 in visited2:
        print(visit2)
    print()

    if array[r][c] == '4' and type == 2:
        if cnt < result:
            result = cnt
            return

    elif array[r][c] == '5' and type == 3:
        if cnt < result:
            result = cnt
            return

    if type == 2:
        visited[r][c] = cnt
        if r != 0 and r != N-1:
            a = 1
            if array[r-1][c] == 1 or array[r-1][c-1] == 1 or array[r-1][c+1] == 1 or array[r+1][c] == 1 or array[r+1][c-1] == 1 or array[r+1][c+1] == 1:
                a = 0
            if a:
                if visited2[r][c] != -1 and visited2[r][c] > cnt+1 or visited2[r][c] == -1:
                    move(r, c, cnt+1, 3)

    elif type == 3:
        visited2[r][c] = cnt

        if c != 0 and c != N-1:
            a = 1
            if array[r-1][c+1] == 1 or array[r+1][c+1] == 1 or array[r][c+1] == 1 or array[r+1][c-1] == 1 or array[r-1][c-1] == 1 or array[r][c-1] == 1:
                a = 0
            if a:

                if visited[r][c] != -1 and visited[r][c] > cnt+1 or visited[r][c] == -1:
                    move(r, c, cnt+1, 2)

    for i in range(4):
        nr = r + next[i][0]
        nc = c + next[i][1]

        if type == 2:
            if nr < 0 or nc < 1 or N <= nr or N-1 <= nc or visited[nr][nc] != -1 and visited[nr][nc] <= cnt+1:
                continue

            if i == 0 or i == 2:
                if array[nr][nc] == 1 or array[nr][nc-1] == 1 or array[nr][nc+1] == 1:
                    continue

            elif i == 1:
                if array[nr][nc+1] == 1:
                    continue

            else:
                if array[nr][nc-1] == 1:
                    continue

            move(nr, nc, cnt+1, 2)


        elif type == 3:
            if nr < 1 or nc < 0 or N-1 <= nr or N <= nc or visited2[nr][nc] != -1 and visited2[nr][nc] <= cnt+1:
                continue

            if i == 1 or i == 3:
                if array[nr][nc] == 1 or array[nr+1][nc] == 1 or array[nr-1][nc] == 1:
                    continue

            elif i == 0:
                if array[nr+1][nc] == 1:
                    continue

            else:
                if array[nr-1][nc] == 1:
                    continue

            move(nr, nc, cnt+1, 3)


N = int(input())

array = []
B = 0
E = 0
start = [0, 0]
for i in range(N):
    row = list(input())
    for j in range(N):
        if row[j] == 'B':
            B += 1
            if B == 2:
                if j < N-1 and row[j+1] == 'B':
                    row[j] = '2'
                else:
                    row[j] = '3'
                start = [i, j]
            else:
                row[j] = '0'

        if row[j] == 'E':
            E += 1
            if E == 2:
                if j < N-1 and row[j+1] == 'E':
                    row[j] = '4'
                else:
                    row[j] = '5'
            else:
                row[j] = '0'
    array.append(row)

result = 99999999999

# 가로
visited = [[-1] * N for _ in range(N)]
# 세로
visited2 = [[-1] * N for _ in range(N)]

move(start[0], start[1], 0, int(array[start[0]][start[1]]))
# print(array[start[0]][start[1]])

print(result)