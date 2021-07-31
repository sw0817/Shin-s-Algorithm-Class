# 백준 1316 그룹 단어 체커
# Baekjoon 1316

# Created by sw0817 on 2021. 07. 31..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1316

N = int(input())
result = 0
for _ in range(N):
    word = input()
    cur = ''
    alpha = set()
    good = True
    for i in range(len(word)):
        alp = word[i]
        if not alp in alpha:
            alpha.add(alp)
        else:
            if not cur == alp:
                good = False
                break
        cur = alp
    if good:
        result += 1

print(result)