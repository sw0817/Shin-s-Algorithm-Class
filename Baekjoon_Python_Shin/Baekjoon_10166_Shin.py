# 백준 10166 관중석
# Baekjoon 10166

# Created by sw0817 on 2022. 04. 27..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10166

D1, D2 = map(int, input().split())
degree = [i for i in range(2001)]

add = 0
for i in range(1, D2 + 1):
    first = True
    for j in range(i * 2, D2 + 1, i):
        if first and D1 <= j and i < D1:
            add += degree[i]
            first = False
        degree[j] -= degree[i]

print(sum(degree[D1:D2 + 1]) + add)