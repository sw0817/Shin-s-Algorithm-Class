# 백준 1875 테스리스
# Baekjoon 1875

# Created by sw0817 on 2021. 07. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1875

from collections import Counter
from copy import deepcopy

one = ["x...x...x",
       "x...x...x",
       "x...x...x",
       "x...x...x"]
two = ["..................",
       "xx..xx.x...x......",
       "x...x..x...xx..xxx",
       "x...x.xx..xxxxx..x"]
three = ["..................",
         "xx..xxx...x.......",
         ".x...xx...x...xxxx",
         ".x...xxx..xxxxxx.."]
four = ["..................",
        "x...x..x...x......",
        "xx..xxxx..xx.x.xxx",
        "x...x..x...xxxx.x."]
five = [".........",
        "...x...x.",
        ".xxxx..xx",
        "xx..x...x"]
six = [".........",
       "....x...x",
       "xx.xx..xx",
       ".xxx...x."]
seven = ["......",
         "......",
         "xx..xx",
         "xx..xx"]
blocks = [[], one, two, three, four, five, six, seven]


def cal(arr2):
    # for row in arr2:
    #     print(row)
    # print()
    global result
    # c = 0
    c = 4*N
    for i in range(4*N):
        # if Counter(arr2[i])['.'] == 3 or Counter(arr2[i])['x'] == 3:
        #     continue
        # c += 1
        if Counter(arr2[i])['.'] == 3:
            c -= 1
        else:
            break
    result = min(result, c)
    return


def check(array, n, cnt):
    global result
    for i in range(len(blocks[n][0])//3):
        # cur_arr = array.copy()
        cur_arr = deepcopy(array)
        h = 4*N+3-(cnt*4)
        while h < 4*N and Counter(cur_arr[h])['.'] == 3:
            h += 1

        if h == 4*N:
            h -= 1

        while h < 4*N:
            stop = False
            for j in range(3):
                if blocks[n][3][3*i+j] == cur_arr[h][j] == 'x' or blocks[n][2][3*i+j] == cur_arr[h-1][j] == 'x' or blocks[n][1][3*i+j] == cur_arr[h-2][j] == 'x' or blocks[n][0][3*i+j] == cur_arr[h-3][j] == 'x':
                    stop = True
                    break
            if stop:
                break
            h += 1

        h -= 1
        stop = False
        for j in range(4):
            if stop:
                break
            for k in range(3):
                # if cur_arr[h-j][k] == '.':
                #     cur_arr[h-j][k] = blocks[n][3-j][3*i+k]
                if blocks[n][3-j][3*i+k] == 'x':
                    cur_arr[h-j][k] = 'x'
                    if result <= 4*N-(h-j):
                        stop = True
                        break
            # if Counter(cur_arr[h-j])['x'] == 3:
            #     for k in range(3):
            #         cur_arr[h-j][k] = '.'
        if stop:
            continue

        if cnt == N:
            # cal(cur_arr.copy())
            cal(deepcopy(cur_arr))
            return

        else:
            # check(cur_arr.copy(), tetris[cnt], cnt+1)
            check(deepcopy(cur_arr), tetris[cnt], cnt + 1)


N = int(input())
arr = [["."] * 3 for _ in range(4*N)]
result = 4*N
tetris = []
for i in range(N):
    tetris.append(int(input()))

check(arr, tetris[0], 1)

print(result)

