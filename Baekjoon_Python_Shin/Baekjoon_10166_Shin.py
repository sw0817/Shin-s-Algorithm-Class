# 백준 10166 관중석
# Baekjoon 10166

# Created by sw0817 on 2022. 04. 27..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10166

from math import gcd

D1, D2 = map(int, input().split())
visited = [[0] * 2001 for _ in range(2001)]
result = 0

for i in range(D1, D2+1):
    for j in range(1, i+1):
        g = gcd(i, j)
        if not visited[i//g][j//g]:
            visited[i//g][j//g] = 1
            result += 1

print(result)