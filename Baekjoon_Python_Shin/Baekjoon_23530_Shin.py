# 백준 23530 Not A + B
# Baekjoon 23530

# Created by sw0817 on 2021. 11. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/23530

for _ in range(int(input())):
    A, B = map(int, input().split())
    if A + B != 1:
        print(1)
    else:
        print(2)