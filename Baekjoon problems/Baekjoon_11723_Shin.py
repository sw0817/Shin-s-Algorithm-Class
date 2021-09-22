# 백준 11723 집합
# Baekjoon 11723

# Created by sw0817 on 2021. 09. 22..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11723

from sys import stdin

S = 1
M = int(stdin.readline())

for _ in range(M):
    info = list(stdin.readline().split())
    if len(info) == 1:
        if info[0] == 'all':
            S = 2 ** 21 - 1
        else:
            S = 1
    else:
        command, target = info[0], int(info[1])
        if command == 'add':
            S |= 2 ** target
        elif command == 'remove':
            S ^= S & 2 ** target
        elif command == 'check':
            if S & 2 ** target:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if S & 2 ** target:
                S ^= S & 2 ** target
            else:
                S |= 2 ** target