# 백준 2455 지능형 기차
# Baekjoon 2455

# Created by sw0817 on 2022. 11. 20..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2455

n = 0
result = 0
for _ in range(4):
    m, p = map(int, input().split())
    n += p - m
    result = max(result, n)

print(result)