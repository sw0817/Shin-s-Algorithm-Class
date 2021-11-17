# 백준 1612 가지고 노는 1
# Baekjoon 1612

# Created by sw0817 on 2021. 11. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1612

N = int(input())

if not N % 2 or not N % 5:
    print(-1)
else:
    result = 1
    n = 1
    while n % N:
        n = (n % N) * 10 + 1
        result += 1

    print(result)