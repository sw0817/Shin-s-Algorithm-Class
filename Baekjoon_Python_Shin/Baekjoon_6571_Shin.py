# 백준 6571 피보나치 수의 개수
# Baekjoon 6571

# Created by sw0817 on 2021. 11. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/6571

fibo = [1, 2]
a, b = 1, 2
while True:
    c = a + b
    fibo.append(c)
    a, b = b, c
    if 10 ** 100 <= c:
        break

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    s, e = 0, 0
    for i in range(len(fibo)):
        if a <= fibo[i]:
            s = i
            break

    for i in range(s, len(fibo)):
        if b < fibo[i]:
            e = i
            break

    print(e - s)