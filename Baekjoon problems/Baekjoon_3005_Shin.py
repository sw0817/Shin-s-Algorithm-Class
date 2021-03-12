# 백준 3005 크로스워드 퍼즐 쳐다보기
# Baekjoon 3005

# Created by sw0817 on 2021. 03. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3005

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
strings = []
for i in range(R):
    string = ''
    for j in range(C):
        if arr[i][j] == '#':
            if 2 <= len(string):
                strings.append(string)
            string = ''
        else:
            string += arr[i][j]
    if 2 <= len(string):
        strings.append(string)

for i in range(C):
    string = ''
    for j in range(R):
        if arr[j][i] == '#':
            if 2 <= len(string):
                strings.append(string)
            string = ''
        else:
            string += arr[j][i]
    if 2 <= len(string):
        strings.append(string)

strings.sort()

print(strings[0])