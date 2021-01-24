# 백준 1446 지름길
# Baekjoon 1446

# Created by sw0817 on 2021. 01. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1446

def go(l, w, idx):
    global result
    for i in range(idx, N):
        start, end, weight = map(int, roads[i])
        if l <= start and end <= D and weight < end - start:
            go(end, w+weight+start-l, i+1)
    if D - l + w <= result:
        result = D - l + w


N, D = map(int, input().split())
result = 10000
roads = [list(map(int, input().split())) for _ in range(N)]
roads.sort()

go(0, 0, 0)
print(result)