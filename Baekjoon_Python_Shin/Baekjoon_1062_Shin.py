# 백준 1062 가르침
# Baekjoon 1062

# Created by sw0817 on 2022. 03. 30..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1062

from itertools import combinations

def makeWords(lst):
    ret = 0
    for word in words:
        for w in word:
            if w not in lst:
                break
        else:
            ret += 1

    return ret


N, K = map(int, input().split())
words = []

for _ in range(N):
    word = input()
    words.append(word)

max_cnt = 0
if K < 5:
    print(0)
else:
    K -= 5
    basic = ['a', 'c', 'i', 'n', 't']
    for comb in list(combinations(list('bdefghjklmopqrsuvwxyz'), K)):
        usable = basic + list(comb)
        max_cnt = max(max_cnt, makeWords(usable))

    print(max_cnt)
