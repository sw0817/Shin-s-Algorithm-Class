# 백준 8901 화학 제품
# Baekjoon 8901

# Created by sw0817 on 2022. 05. 02..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/8901

T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    costs = list(map(int, input().split()))
    result = 0
    for i in range(min(A, B) + 1):
        a, b, c = A, B, C
        cur = costs[0] * i
        for j in range(min(b-i, c) + 1):
            result = max(result, cur + costs[1] * j + costs[2] * (min(a-i, c-j)))
    print(result)
