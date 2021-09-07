# 백준 1959 달팽이3
# Baekjoon 1959

# Created by sw0817 on 2021. 09. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1959

M, N = map(int, input().split())

result = 0
endPoint = [0, 0]

if 2 < M and 2 < N:
    a = min(M // 2, N // 2)
    result += a * 4 - 1
    endPoint = [a+1, a]
    M -= a * 2
    N -= a * 2

    if M == 0 or N == 0:
        if M == 0:
            result -= 1
    elif M == 1:
        endPoint[1] += N
        result += 1
    elif N == 1:
        result += 2
        endPoint[0] += M - 1
        endPoint[1] += 1
else:
    if M == 2:
        result = 2
        endPoint = [2, 1]
    elif N == 2:
        result = 3
        endPoint = [2, 1]

print(result)
print(*endPoint)