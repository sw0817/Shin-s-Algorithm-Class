# 백준 8972 미친 아두이노
# Baekjoon 8972

# Created by sw0817 on 2021. 10. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/8972

R, C = map(int, input().split())
arr = []
arduino = []
for i in range(R):
    row = list(input())
    for j in range(C):
        if row[j] == 'I':
            start = (i, j)
        elif row[j] == 'R':
            arduino.append((i, j))
    arr.append(row)

info = input()
l = len(info)
cnt = 0
move = [(), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
for i in range(l):
    save = True
    r, c = start
    dr, dc = move[int(info[i])]
    nr, nc = r + dr, c + dc
    cnt += 1
    nxt_arduino = set()
    break_arduino = []
    for r, c in arduino:
        if r < nr:
            r += 1
        elif nr < r:
            r -= 1
        if c < nc:
            c += 1
        elif nc < c:
            c -= 1
        if (r, c) in nxt_arduino:
            break_arduino.append((r, c))
        nxt_arduino.add((r, c))

    if (nr, nc) in nxt_arduino:
        print("kraj {}".format(cnt))
        save = False
        break

    for ard in break_arduino:
        nxt_arduino.discard(ard)
    arduino = list(nxt_arduino)

    start = (nr, nc)

if save:
    final = [['.'] * C for _ in range(R)]
    final[start[0]][start[1]] = 'I'
    for r, c in arduino:
        final[r][c] = 'R'

    for i in range(R):
        print(''.join(final[i]))