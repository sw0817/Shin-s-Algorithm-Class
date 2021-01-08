# 백준 1149 볼링 점수 계산
# Baekjoon 1149

# Created by sw0817 on 2021. 01. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1149

N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i - 1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i - 1][1]) + RGB[i][2]

print(min(RGB[N-1]))

