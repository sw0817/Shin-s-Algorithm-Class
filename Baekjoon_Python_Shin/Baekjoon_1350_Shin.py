# 백준 1350 진짜 공간
# Baekjoon 1350

# Created by sw0817 on 2022. 01. 16..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1350

N = int(input())
files = list(map(int, input().split()))
c = int(input())

result = 0
for file in files:
    if file:
        m = file // c
        if file % c:
            result += 1
        result += m

print(result * c)