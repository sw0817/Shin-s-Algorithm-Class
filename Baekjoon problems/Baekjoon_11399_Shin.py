# 백준 11399 ATM
# Baekjoon 11399

# Created by sw0817 on 2021. 06. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11399

N = int(input())
Ps = list(map(int, input().split()))
# 빨리 끝내고 가야 덜 기다림
Ps.sort()
result = 0
# 앞 사람일수록 여러명이 기다림
for i in range(N):
    result += Ps[i] * (N-i)

print(result)