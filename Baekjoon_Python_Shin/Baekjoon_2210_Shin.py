# 백준 2210 숫자판 점프
# Baekjoon 2210

# Created by sw0817 on 2022. 01. 25..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2210

def makeNum(l, r, c, num):
    if l == 6:
        nums.add(num)
        return

    for dr, dc in move:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            makeNum(l+1, nr, nc, num+arr[nr][nc])


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

arr = [list(map(str, input().split())) for _ in range(5)]
nums = set()
for i in range(5):
    for j in range(5):
        makeNum(1, i, j, arr[i][j])

print(len(nums))