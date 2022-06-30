# 백준 1264 모음의 개수
# Baekjoon 1264

# Created by sw0817 on 2022. 06. 30..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1264

aeiou = 'aeiouAEIOU'

while True:
    sentence = input()
    if sentence == '#':
        break
    n = 0
    for s in sentence:
        if s in aeiou:
            n += 1
    print(n)