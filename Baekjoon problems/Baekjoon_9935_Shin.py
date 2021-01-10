# 백준 9935 문자열 폭발
# Baekjoon 9935

# Created by sw0817 on 2021. 01. 10..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9935

text = input()
bomb = input()

last = bomb[-1]
l = len(bomb)

explosion = []

for char in text:
    explosion.append(char)
    if char == last and ''.join(explosion[-l:]) == bomb:
        del explosion[-l:]

if explosion:
    print(''.join(explosion))

else:
    print('FRULA')