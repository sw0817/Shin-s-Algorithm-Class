# 백준 11918 정전
# Baekjoon 11918

# Created by sw0817 on 2021. 12. 01..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11918

N, L = map(int, input().split())
OJ = list(map(int, input().split()))
OJ.sort()

result = 0
prev = OJ[0] + L
last = OJ[0] - L
for i in range(1, N):
    cur = max(last, OJ[i] - L)
    if cur < prev:
        result += prev - cur
    last = max(prev, OJ[i] - L)
    prev = OJ[i] + L

print(result)