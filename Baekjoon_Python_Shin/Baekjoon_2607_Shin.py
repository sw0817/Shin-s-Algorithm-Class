# 백준 2607 비슷한 단어
# Baekjoon 2607

# Created by sw0817 on 2021. 08. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2607

N = int(input())
result = 0
initial_word = list(input())

for _ in range(N-1):
    word = initial_word[:]
    check = list(input())
    for _ in range(len(check)):
        w = check.pop(0)
        if w in word:
            word.remove(w)
        else:
            check.append(w)

    a, b = len(word), len(check)
    if a in [0, 1] and b in [0, 1]:
        result += 1

print(result)