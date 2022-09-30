# 백준 5532 방학 숙제
# Baekjoon 5532

# Created by sw0817 on 2022. 09. 30..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5532

L = int(input()); A = int(input()); B = int(input()); C = int(input()); D = int(input())

print(L - max(A // C + 1 if A % C else A // C, B // D + 1 if B % D else B // D))