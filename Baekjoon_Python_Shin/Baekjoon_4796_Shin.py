# 백준 4796 캠핑
# Baekjoon 4796

# Created by sw0817 on 2022. 01. 18..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4796

t = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break

    cycle = V // P
    remain = V % P
    print('Case {}: {}'.format(t, cycle * L + min(remain, L)))
    t += 1