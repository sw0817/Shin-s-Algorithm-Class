# 백준 1629 곱셈
# Baekjoon 1629

# Created by sw0817 on 2021. 01. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1629

def cal(a, b):
    if b == 1:
        return a % C
    else:
        bb = cal(a, b // 2)
        if b % 2 == 0:
            return bb * bb % C
        else:
            return bb * bb * a % C


A, B, C = map(int, input().split())

print(cal(A, B))