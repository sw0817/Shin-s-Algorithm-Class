# 백준 10166 관중석
# Baekjoon 10166

# Created by sw0817 on 2022. 04. 27..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10166

D1, D2 = map(int, input().split())
dir = set()
dir.add(0)

for i in range(D1, D2+1):
    for j in range(1, i):
        dir.add(j/i)

print(len(dir))