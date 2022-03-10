# 백준 1946 신입 사원
# Baekjoon 1946

# Created by sw0817 on 2022. 03. 11..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1946

T = int(input())
for _ in range(T):
    N = int(input())
    rate = []
    for _ in range(N):
        rate.append(list(map(int, input().split())))

    rate.sort()
    result = 1
    min_rate = rate[0][1]

    for i in range(1, N):
        if rate[i][1] < min_rate:
            min_rate = rate[i][1]
            result += 1

    print(result)