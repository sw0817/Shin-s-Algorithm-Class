# 백준 2083 럭비 클럽
# Baekjoon 2083

# Created by sw0817 on 2022. 09. 06..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2083

while True:
    n, a, w = list(input().split())

    if n == '#':
        break

    if 17 < int(a) or 80 <= int(w):
        print(n, 'Senior')
    else:
        print(n, 'Junior')