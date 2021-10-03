# 백준 10809 알파벳 찾기
# Baekjoon 10809

# Created by sw0817 on 2021. 06. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10809

word = input()
result = [-1] * 26
for i in range(len(word)):
    al = ord(word[i]) - 97
    if result[al] == -1:
        result[al] = i

print(*result)