# 백준 1284 집 주소
# Baekjoon 1284

# Created by sw0817 on 2022. 09. 08..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1284

while True:
    num = input()
    if num == '0':
        break

    l = 0
    for n in num:
        if n == '1':
            l += 2
        elif n == '0':
            l += 4
        else:
            l += 3

    l += len(num) + 1

    print(l)