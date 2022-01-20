# 백준 1411 비슷한 단어
# Baekjoon 1411

# Created by sw0817 on 2022. 01. 20..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1411

N = int(input())
pat = dict()
for _ in range(N):
    word = input()
    i = 1
    cur = ''
    alp = dict()
    for w in word:
        if w in alp:
            cur += str(alp[w])
        else:
            alp[w] = i
            cur += str(i)
            i += 1

    if cur in pat:
        pat[cur] += 1
    else:
        pat[cur] = 1

result = 0
for p in pat:
    c = pat[p]
    if 1 < c:
        result += c * (c-1) // 2

print(result)