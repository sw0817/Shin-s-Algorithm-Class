# SWEA 5215 햄버거 다이어트
# SWEA 5215

# Created by sw0817 on 2020. 12. 10..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE

def select(idx, point, cal):
    global result

    if idx == N:
        if result < point:
            result = point
        return

    if sum(points[idx:]) + point < result:
        return

    if cal + cals[idx] < L:
        select(idx+1, point+points[idx], cal+cals[idx])
    select(idx+1, point, cal)


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())

    points = []
    cals = []

    for i in range(N):
        point, cal = map(int, input().split())
        points.append(point)
        cals.append(cal)

    result = 0

    select(0, 0, 0)

    print('#{} {}'.format(tc, result))