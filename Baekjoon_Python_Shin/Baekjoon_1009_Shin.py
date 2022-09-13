# 백준 1009 분산처리
# Baekjoon 1009

# Created by sw0817 on 2022. 09. 13..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1009

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10
    b = b % 4
    if b == 0:
        b = 4
    s = a ** b % 10
    print(s if s else 10)