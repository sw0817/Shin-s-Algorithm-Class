# 백준 2739 구구단
# Baekjoon 2739

# Created by sw0817 on 2021. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2739

N = int(input())

for i in range(1, 10):
    print('{} * {} = {}'.format(N, i, N*i))