# 백준 1013 Contact
# Baekjoon 1013

# Created by sw0817 on 2021. 09. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1013

import re

N = int(input())
p = re.compile('(100+1+|01)+')
for _ in range(N):
    wave = input()
    m = p.fullmatch(wave)
    if m:
        print('YES')
    else:
        print('NO')
