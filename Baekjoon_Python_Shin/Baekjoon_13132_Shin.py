# 백준 13132 World Cup
# Baekjoon 13132

# Created by sw0817 on 2021. 08. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/13132

def recur(m, n, p):
    global result
    if m <= B:
        return
    if n == N:
        if 100 < m:
            result += p
        return

    upMoney = m + m * M * (info[n][1]-1)
    upPer = info[n][0] * p
    downMoney = m - m * M
    downPer = p - upPer
    recur(upMoney, n+1, upPer)
    recur(downMoney, n+1, downPer)


N, M, B = map(int, input().split())
M /= 100
info = []
result = 0

for _ in range(N):
    P, R = map(float, input().split())
    P /= 100
    info.append((P, R))

recur(100, 0, 100)
print(result)

