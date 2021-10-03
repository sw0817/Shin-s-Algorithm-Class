# 백준 1231 주식왕 동호
# Baekjoon 1231

# Created by sw0817 on 2021. 07. 12..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1231

C, D, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]
result = [i for i in range(500001)]

for j in range(1, D):
    for i in range(C):
        prev = arr[i][j-1]
        price = arr[i][j]
        for k in range(prev, M+1):
            temp = result[k-prev] + price
            if result[k] < temp:
                result[k] = temp
    M = result[M]
    for i in range(M+1):
        result[i] = i

print(M)