# 백준 2675 문자열 반복
# Baekjoon 2675

# Created by sw0817 on 2021. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2675

T = int(input())

for _ in range(T):
    N, S = map(str, input().split())
    N = int(N)
    for i in range(len(S)):
        for _ in range(N):
            print(S[i], end='')

    print()