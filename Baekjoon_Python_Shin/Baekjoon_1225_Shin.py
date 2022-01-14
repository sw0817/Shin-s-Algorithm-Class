# 백준 1225 이상한 곱셈
# Baekjoon 1225

# Created by sw0817 on 2022. 01. 14..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1225

A, B = map(str, input().split())
a = b = 0

for i in A:
    a += int(i)

for i in B:
    b += int(i)

print(a*b)