# 백준 1132 합
# Baekjoon 1132

# Created by sw0817 on 2021. 07. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1132

N = int(input())
alpha = [[0] for _ in range(10)]
exist = [0] * 10
for i in range(10):
    alpha[i].append(chr(65+i))
first = set()

for _ in range(N):
    num = input()
    first.add(num[0])
    exist[ord(num[0])] = 1
    l = len(num)
    for i in range(l):
        alp = ord(num[l-i-1])-65
        alpha[alp][0] += 10 ** i

alpha.sort(reverse=True)

# 중간 점검

