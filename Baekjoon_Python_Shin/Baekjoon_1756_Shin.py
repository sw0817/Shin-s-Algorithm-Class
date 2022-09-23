# 백준 1756 피자 굽기
# Baekjoon 1756

# Created by sw0817 on 2022. 09. 23..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1756

def solution():
    D, N = map(int, input().split())
    ds = list(map(int, input().split()))
    pizza = list(map(int, input().split()))

    cur = ds[0]
    for i in range(1, D):
        if ds[i] < cur:
            cur = ds[i]
        else:
            ds[i] = cur

    c = 0
    for i in range(N):
        p = pizza[i]
        while ds and ds[-1] < p:
            c += 1
            ds.pop(-1)

        if not ds:
            print(0)
            return

        c += 1
        ds.pop(-1)

    print(D - c + 1)

solution()