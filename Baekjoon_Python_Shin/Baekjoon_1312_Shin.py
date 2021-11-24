# 백준 1312 소수
# Baekjoon 1312

# Created by sw0817 on 2021. 11. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1312

A, B, N = map(int, input().split())
A %= B
for i in range(N-1):
    A = (A * 10) % B
print((A * 10) // B)