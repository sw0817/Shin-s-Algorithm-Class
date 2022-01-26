# 백준 2877 4와 7
# Baekjoon 2877

# Created by sw0817 on 2022. 01. 26..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2877

K = int(input())
cnt = 0
n = 0
answer = []
result = ''

while 1:
    n += 1
    cnt += 2 ** n
    if cnt >= K:
        break

idx = K - 2 ** n + 1
for i in range(n):
    answer.append(idx % 2)
    idx //= 2

answer.reverse()
for i in range(len(answer)):
    if answer[i] == 1:
        result += '7'
    else:
        result += '4'

print(int(result))