# 백준 15552 빠른 A+B
# Baekjoon 15552

# Created by sw0817 on 2020. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15552

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)