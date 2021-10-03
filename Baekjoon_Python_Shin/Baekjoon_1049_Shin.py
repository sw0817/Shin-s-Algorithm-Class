# 백준 1049 기타줄
# Baekjoon 1049

# Created by sw0817 on 2020. 12. 18..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1049

N, M = map(int, input().split())
six_price = 1000
one_price = 1000

for _ in range(M):
    six, one = map(int, input().split())
    if six < six_price:
        six_price = six
    if one < one_price:
        one_price = one

if one_price * 6 <= six_price:
    result = one_price * N

else:
    confirm = N // 6
    remainder = N % 6

    result = confirm * six_price

    if remainder * one_price <= six_price:
        result += remainder * one_price
    else:
        result += six_price

print(result)
