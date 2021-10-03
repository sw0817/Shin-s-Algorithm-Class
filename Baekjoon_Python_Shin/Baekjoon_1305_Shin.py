# 백준 1305 박성원
# Baekjoon 1305

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1305

L = int(input())
word = input()

pi = [0 for _ in range(L)]
j = 0
for i in range(1, L):

    while j > 0 and word[i] != word[j]:
        j = pi[j-1]

    if word[i] == word[j]:
        j += 1
        pi[i] = j

print(L - pi[L-1])
