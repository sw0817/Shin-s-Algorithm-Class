# 백준 2920 음계
# Baekjoon 2920

# Created by sw0817 on 2021. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2920

numbers = list(map(int, input().split()))

if numbers[0] == 1:
    for i in range(1, 8):
        if numbers[i] != i+1:
            print('mixed')
            break
        if i == 7:
            print('ascending')

elif numbers[0] == 8:
    for i in range(1, 8):
        if numbers[i] != 8-i:
            print('mixed')
            break
        if i == 7:
            print('descending')
else:
    print('mixed')