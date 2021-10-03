# 백준 2908 상수
# Baekjoon 2908

# Created by sw0817 on 2021. 06. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2908

A, B = map(str, input().split())
a, b = "", ""
for i in range(3):
    a += A[2-i]
    b += B[2-i]

a, b = int(a), int(b)
if a > b:
    print(a)
else:
    print(b)