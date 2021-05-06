# 백준 2292 벌집
# Baekjoon 2292

# Created by sw0817 on 2021. 05. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2292

N = int(input())
if N == 1:
    print(1)
else:
    cnt = 1
    x = 1
    num = 1
    while True:
        num += x * 6
        cnt += 1
        if N <= num:
            print(cnt)
            break
        x += 1

