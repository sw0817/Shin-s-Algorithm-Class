# 백준 2010 플러그
# Baekjoon 2010

# Created by sw0817 on 2022. 09. 04..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2010

N = int(input())
for _ in range(N):
    N -= int(input())

print(abs(N - 1))