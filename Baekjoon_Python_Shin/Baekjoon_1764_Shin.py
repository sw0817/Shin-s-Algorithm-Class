# 백준 1764 듣보잡
# Baekjoon 1764

# Created by sw0817 on 2021. 11. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1764

N, M = map(int, input().split())

firstSet = set()
for _ in range(N):
    firstSet.add(input())

result = []
for _ in range(M):
    name = input()
    if name in firstSet:
        result.append(name)

result.sort()
print(len(result))
for name in result:
    print(name)