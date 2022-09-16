# 백준 2525 오븐 시계
# Baekjoon 2525

# Created by sw0817 on 2022. 09. 16..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2525

A, B = map(int, input().split())
C = int(input())
D = B + C
print((A + D // 60) % 24, D % 60)