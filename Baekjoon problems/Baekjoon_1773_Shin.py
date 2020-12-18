# 백준 1773 기타줄
# Baekjoon 1773

# Created by sw0817 on 2020. 12. 18..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1773

N, C = map(int, input().split())

check = [0] * C
result = 0
for _ in range(N):
    T = int(input())
    for i in range(T-1, C, T):
        if not check[i]:
            check[i] = 1
            result += 1

print(result)