# 백준 1254 팰린드롬 만들기
# Baekjoon 1254

# Created by sw0817 on 2021. 09. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1254

word = input()
l = len(word)
for i in range(l):
    if word[i:] == word[i:][::-1]:
        print(len(word)+i)
        break