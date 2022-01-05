# 백준 8979 올림픽
# Baekjoon 8979

# Created by sw0817 on 2022. 01. 05..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/8979

N, K = map(int, input().split())
cnt = 0
prize = 0
medal = [0, 0, 0]
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))

info.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)
for i in range(N):
    cnt += 1
    if info[i][1:] != medal:
        prize = cnt
        medal = info[i][1:]
    if info[i][0] == K:
        print(prize)
        break