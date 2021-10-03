# 백준 1380 귀걸이
# Baekjoon 1380

# Created by sw0817 on 2021. 09. 03..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1380

scene = 1
while True:
    N = int(input())
    if not N:
        break
    names = []
    check = [0] * N
    for _ in range(N):
        names.append(input())
    for _ in range(2 * N - 1):
        idx, alp = map(str, input().split())
        check[int(idx)-1] += 1
    print(scene, names[check.index(1)])
    scene += 1