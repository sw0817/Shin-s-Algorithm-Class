# 백준 5541 釘 (Nails)
# Baekjoon 5541

# Created by sw0817 on 2021. 09. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5541

N, M = map(int, input().split())
imos = [[0] * (N+3) for _ in range(N+3)]
for _ in range(M):
    a, b, c = map(int, input().split())
    imos[a][b] += 1
    imos[a][b+1] -= 1
    imos[a+c+1][b] -= 1
    imos[a+c+2][b+1] += 1
    imos[a+c+1][b+c+2] += 1
    imos[a+c+2][b+c+2] -= 1

# 대각선
for i in range(1, N):
    y = 1
    x = N - i + 1
    while x <= N:
        imos[y][x] += imos[y-1][x-1]
        y += 1
        x += 1

for i in range(1, N+1):
    y = i
    x = 1
    while y <= N:
        imos[y][x] += imos[y-1][x-1]
        y += 1
        x += 1

# 밑으로
for y in range(1, N+1):
    for x in range(1, y+1):
        imos[y][x] += imos[y-1][x]

# 오른쪽으로
for y in range(1, N+1):
    for x in range(1, y+1):
        imos[y][x] += imos[y][x-1]

cnt = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        if imos[i][j]:
            cnt += 1

print(cnt)