# 백준 15686 치킨 배달
# Baekjoon 15686

# Created by sw0817 on 2021. 02. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15686

from itertools import combinations


N, M = map(int, input().split())
C = []
H = []
arr = []
result = 999999
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(N):
        if row[j] == 1:
            H.append((i, j))
        elif row[j] == 2:
            C.append((i, j))

# 치킨 집 고르는 모든 조합에 대해 가장 짧은 치킨 거리 구하기
for comb in combinations(C, M):
    dist = 0
    for i, j in H:
        dist_chicken = 999999
        for r, c in comb:
            if abs(i-r) + abs(j-c) < dist_chicken:
                dist_chicken = abs(i-r) + abs(j-c)
        dist += dist_chicken
        if result <= dist:
            break

    if dist < result:
        result = dist

print(result)