# 백준 10993 별 찍기 - 18
# Baekjoon 10993

# Created by sw0817 on 2021. 12. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10993

N = int(input())
star = [[' '] * (2 * (2 ** N - 1) - 1) for _ in range(2 ** N - 1)]

if N % 2:
    up = True
    initial = True
else:
    up = False
    initial = False

top = 0
bottom = 2 ** N - 2
left = 0
right = 2 * (2 ** N - 1) - 2
middle = (top + bottom) // 2

while N:
    if up:
        for j in range(left, right+1):
            star[bottom][j] = '*'
        for i in range(bottom - top + 1):
            star[bottom-i][left+i] = '*'
            star[bottom-i][right-i] = '*'
        up = False
        top = middle
        bottom -= 1

    else:
        for j in range(left, right+1):
            star[top][j] = '*'
        for i in range(bottom - top + 1):
            star[top+i][left+i] = '*'
            star[top+i][right-i] = '*'
        up = True
        bottom = middle
        top += 1

    left += (2 ** N) // 2
    right -= (2 ** N) // 2
    N -= 1
    middle = (top + bottom) // 2

l = len(star[0])
l2 = len(star)

if initial:
    for i in range(l2):
        print(''.join(star[i][:1+l//2+i]))
else:
    for i in range(l2):
        print(''.join(star[i][:l-i]))