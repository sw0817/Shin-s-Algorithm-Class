# 백준 11720 숫자의 합
# Baekjoon 11720

# Created by sw0817 on 2021. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11720

N = int(input())
number = input()

result = 0
for i in range(N):
    result += int(number[i])

print(result)