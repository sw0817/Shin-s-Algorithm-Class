# 백준 15829 Hashing
# Baekjoon 15829

# Created by sw0817 on 2022. 01. 03..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/15829

L = int(input())
st = input()
r = 31
M = 1234567891
result = 0
for i in range(L):
    result += (ord(st[i]) - 96) * (r ** i)
    result %= M

print(result)