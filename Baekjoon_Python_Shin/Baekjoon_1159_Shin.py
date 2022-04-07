# 백준 1159 농구 경기
# Baekjoon 1159

# Created by sw0817 on 2022. 04. 07..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1159

N = int(input())
last = set()
names = dict()
for _ in range(N):
    name = input()[0]
    if name in names:
        names[name] += 1
        if 5 <= names[name]:
            last.add(name)
    else:
        names[name] = 1

last = sorted(list(last))
print(''.join(last) if last else 'PREDAJA')