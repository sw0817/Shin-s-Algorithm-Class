# SWEA 5656 벽돌 깨기
# SWEA 5656

# Created by sw0817 on 2020. 12. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE

from copy import deepcopy


nexts = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 남은 구슬 갯수, 현재 배열 상태, 현재 폭발력, 현재 위치, 현재 위치
def bomb(power, r, c):
    arr2[r][c] = 0
    for i in range(1, power):
        for dr, dc in nexts:
            nr = r + (dr*i)
            nc = c + (dc*i)
            if 0 <= nr < H and 0 <= nc < W:
                if arr2[nr][nc] == 1:
                    arr2[nr][nc] = 0
                elif arr2[nr][nc] > 1:
                    bomb(arr2[nr][nc], nr, nc)


def after():
    for j in range(W):
        stack = []
        for i in range(H):
            if arr2[i][j] > 0:
                stack.append(arr2[i][j])
                arr2[i][j] = 0
        i = H-1
        while stack:
            arr2[i][j] = stack.pop()
            i -= 1


def choice(n, arr3, r, c):
    global result
    arr2 = deepcopy(arr3)
    bomb(arr2[r][c], r, c)
    if n == 0:
        temp = 0
        for i in range(H):
            for j in range(W):
                if arr2[i][j] > 0:
                    temp += 1
        if result > temp:
            result = temp
        return
    after()
    next_arr = deepcopy(arr2)
    for j in range(W):
        for i in range(H):
            if arr[i][j] > 0:
                choice(n-1, next_arr, i, j)
                break


T = int(input())

for tc in range(1, T+1):

    # 구슬 갯수 N, 가로 길이 W, 세로 길이 H
    N, W, H = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(H)]
    arr2 = [[0] * W for _ in range(H)]
    result = W * H

    initial_arr = deepcopy(arr)
    for j in range(W):
        for i in range(H):
            if arr[i][j] > 0:
                choice(N-1, initial_arr, i, j)
                break

    print(result)