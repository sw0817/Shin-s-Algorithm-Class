# 백준 2170 선 긋기
# Baekjoon 2170

# Created by sw0817 on 2022. 09. 21..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2170

N = int(input())
result = 0
info = []
for _ in range(N):
    info.append(tuple(map(int, input().split())))

info.sort()
curL = -1000000000
for l, r in info:
    if curL <= l:
        result += r - l
    elif curL < r:
        result += r - curL
    curL = max(curL, r)

print(result)