# 백준 9465 스티커
# Baekjoon 9465

# Created by sw0817 on 2021. 01. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9465

T = int(input())
for _ in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]
    for j in range(2, N):
        sticker[0][j] += max(sticker[1][j-1], sticker[1][j-2])
        sticker[1][j] += max(sticker[0][j-1], sticker[0][j-2])
    print(max(sticker[0][N-1], sticker[1][N-1]))