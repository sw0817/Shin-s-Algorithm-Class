# 백준 10814 나이순 정렬
# Baekjoon 10814

# Created by sw0817 on 2021. 04. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10814

from sys import stdin

N = int(stdin.readline())
sorting = []
for i in range(N):
    info = list(map(str, stdin.readline().split()))
    sorting.append(info)

sorting.sort(key=lambda x: (int(x[0])))
for i in range(N):
    print(*sorting[i])