# 백준 2034 반음
# Baekjoon 2034

# Created by sw0817 on 2022. 04. 12..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2034

def check(idx):
    temp = piano[idx] + ' '
    for i in range(n):
        idx = (idx + nxt[i]) % l
        if piano[idx] == 'x':
            return
    result.append(temp + piano[idx])
    return


n = int(input())
piano = list('AxBCxDxEFxGx')
l = len(piano)
result = []

nxt = []
for _ in range(n):
    nxt.append(int(input()))

for i in range(l):
    check(i)

result.sort()
for r in result:
    print(r)