# 백준 1895 필터
# Baekjoon 1895

# Created by sw0817 on 2021. 07. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1895

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

# flt = [[0] * (C-2) for _ in range(R-2)]
result = 0

for j in range(C-2):
    f = arr[0][j:j+3] + arr[1][j:j+3]
    # f = (arr[0][j:j+2] + arr[1][j:j+2])
    # print(f)
    for i in range(R-2):
        f.extend(arr[i+2][j:j+3])
        # print(f)
        sf = sorted(f)
        # print(sf)
        # flt[i][j] = sf[4]
        if T <= sf[4]:
            result += 1
        f = f[3:]

# for row in flt:
#     print(*row)

print(result)