# 백준 2312 수 복원하기
# Baekjoon 2312

# Created by sw0817 on 2022. 11. 15..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2312

for _ in range(int(input())):
    N = int(input())
    n = 2
    d = dict()
    while n <= N:
        if not N % n:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            N //= n
        else:
            n += 1

    for s in d:
        print(s, d[s])