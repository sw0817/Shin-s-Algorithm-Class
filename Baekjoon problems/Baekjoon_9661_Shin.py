# 백준 9661 돌 게임 7
# Baekjoon 9661

# Created by sw0817 on 2021. 06. 16..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9661

N = int(input())
if N % 5 == 0 or N % 5 == 2:
    print("CY")
else:
    print("SK")