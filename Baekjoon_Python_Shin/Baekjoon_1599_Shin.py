# 백준 1599 민식어
# Baekjoon 1599

# Created by sw0817 on 2022. 03. 13..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1599

alp = ["a", "b", "k", "d", "e", "g", "h", "i", "l", "m", "n", "ng", "o", "p", "r", "s", "t", "u", "w", "y"]

N = int(input())
words = []
for _ in range(N):
    word = []
    read = input()
    l = len(read)
    idx = 0
    while idx < l:
        w = read[idx]
        if w == "n" and idx < l - 1 and read[idx+1] == "g":
            word.append(alp.index("ng"))
            idx += 2
            continue
        else:
            word.append(alp.index(w))
            idx += 1
    words.append(word)

words.sort()
for word in words:
    answer = ""
    for w in word:
        answer += alp[w]
    print(answer)