# 백준 14725 개미굴
# Baekjoon 14725

# Created by sw0817 on 2021. 03. 22..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14725

N = int(input())
order = []
max_K = 0
for _ in range(N):
    info = list(input().split())
    K = int(info[0])
    if max_K < K:
        max_K = K
    info = info[1:]
    order.append(info)

cur_floor = [False] * max_K
order.sort()
pointer = 0

for i in range(N):
    for j in range(len(order[i])):
        if cur_floor[j] == order[i][j] and j <= pointer:
            continue
        else:
            pointer = j
            cur_floor[j] = order[i][j]
            floor = '--' * j
            print('{}{}'.format(floor, cur_floor[j]))
