# 백준 10952 A+B - 5
# Baekjoon 10952

# Created by sw0817 on 2021. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10952

while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    print(A+B)