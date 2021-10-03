# 백준 1251 단어 나누기
# Baekjoon 1251

# Created by sw0817 on 2021. 08. 22..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1251

word = input()

wordList = []
l = len(word)
for i in range(1, l-1):
    for j in range(i+1, l):
        wordList.append("".join(reversed(word[:i])) + "".join(reversed(word[i:j])) + "".join(reversed(word[j:])))

wordList.sort()
print(wordList[0])