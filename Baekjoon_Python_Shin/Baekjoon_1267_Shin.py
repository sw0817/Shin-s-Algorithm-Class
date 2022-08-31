# 백준 1267 핸드폰 요금
# Baekjoon 1267

# Created by sw0817 on 2022. 08. 31..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1267

input()
Y = 0
M = 0
for c in list(map(int, input().split())):
    c += 1
    Y += c // 30 * 10 if not c % 30 else c // 30 * 10 + 10
    M += c // 60 * 15 if not c % 60 else c // 60 * 15 + 15

if Y <= M:
    print('Y', end=' ')
if M <= Y:
    print('M', end=' ')
print(min(Y, M))