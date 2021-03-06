# 백준 4355 서로소
# Baekjoon 4355

# Created by sw0817 on 2021. 03. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4355

while True:
    n = int(input())
    if n == 0:
        break

    if n == 1:
        print(1)

    else:
        result = n
        for i in range(2, round(n**0.5)+1):
            if n % i == 0:
                while n % i == 0:
                    n //= i
                result *= 1 - (1/i)
        if n > 1:
            result *= 1 - (1/n)
        print(round(result))