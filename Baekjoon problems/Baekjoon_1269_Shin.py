# 백준 1269 대칭 차집합
# Baekjoon 1269

# Created by sw0817 on 2021. 09. 04..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1269

lenA, lenB = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

setAB = set(A+B)
l = len(setAB)

print(l * 2 - lenA - lenB)
