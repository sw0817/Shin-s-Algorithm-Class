# 백준 1913 달팽이
# Baekjoon 1913

# Created by sw0817 on 2021. 07. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1913

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(input())
t = int(input())

arr = [[0] * N for _ in range(N)]
result = []

r, c = (N-1) // 2, (N-1) // 2
arr[r][c] = 1
d = 0
cnt = 0
temp = 1
n = 2
while temp < N:
    for _ in range(temp):
        r += move[d][0]
        c += move[d][1]
        arr[r][c] = n
        if n == t:
            result = [r+1, c+1]
        n += 1
    d = (d + 1) % 4
    cnt += 1
    if cnt == 2:
        temp += 1
        cnt = 0

for _ in range(temp-1):
    r += move[d][0]
    arr[r][c] = n
    if n == t:
        result = [r + 1, c + 1]
    n += 1

for row in arr:
    print(*row)

print(*result)