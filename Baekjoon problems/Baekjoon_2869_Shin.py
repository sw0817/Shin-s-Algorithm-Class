# 백준 2869 달팽이는 올라가고 싶다
# Baekjoon 2869

# Created by sw0817 on 2021. 07. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())

if V <= A:
    print(1)
else:
    result = (V-A) // (A-B) + 1
    if result - 1 < (V-A) / (A-B):
        result += 1
    print(result)