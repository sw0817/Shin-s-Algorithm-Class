# 백준 2522 별 찍기 - 12
# Baekjoon 2522

# Created by sw0817 on 2022. 01. 15..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2522

N = int(input())
for i in range(N):
    print(' ' * (N-i-1) + '*' * (i+1))
for i in range(1, N):
    print(' ' * (i) + '*' * (N-i))