# 백준 10951 A+B - 4
# Baekjoon 10951

# Created by sw0817 on 2020. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10951

a = 1
while a:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        a = 0