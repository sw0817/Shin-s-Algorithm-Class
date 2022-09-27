# 백준 1075 나누기
# Baekjoon 1075

# Created by sw0817 on 2022. 09. 27..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1075

N = int(input())
F = int(input())

answer = 99

n = N // 100 * 100
for i in range(100):
    if not (n + i) % F:
        answer = i
        break

if answer == 0:
    print('00')
elif answer < 10:
    print('0' + str(answer))
else:
    print(str(answer))