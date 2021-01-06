# 백준 8958 OX퀴즈
# Baekjoon 8958

# Created by sw0817 on 2020. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/8958

T = int(input())

for _ in range(T):
    ox = input()
    result = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)