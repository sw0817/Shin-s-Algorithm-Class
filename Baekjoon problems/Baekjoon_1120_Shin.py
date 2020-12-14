# 백준 1120 문자열
# Baekjoon 1120

# Created by sw0817 on 2020. 12. 15..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1120


word1, word2 = input().split()
result = len(word1)

for i in range(len(word2)+1 - len(word1)):
    count = 0
    for j in range(len(word1)):
        if word1[j] != word2[i+j]:
            count += 1

    if count < result:
        result = count

print(result)