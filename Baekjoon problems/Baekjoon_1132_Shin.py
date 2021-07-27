# 백준 1132 합
# Baekjoon 1132

# Created by sw0817 on 2021. 07. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1132

N = int(input())
alpha = [[0] for _ in range(10)]
n = [1] * 10
nums = []
nonZero = set()
for i in range(10):
    alpha[i].append(chr(65+i))

for _ in range(N):
    num = input()
    nums.append(num)
    nonZero.add(num[0])
    l = len(num)
    for i in range(l):
        alp = ord(num[l-i-1])-65
        alpha[alp][0] += 10 ** i

alpha.sort()

for i in range(10):
    if not alpha[i][1] in nonZero:
        alpha[i][1] = 0
        break

cnt = 1
for i in range(10):
    if alpha[i][1]:
        alpha[i][1] = cnt
        cnt += 1

result = 0

for info in alpha:
    result += info[0] * info[1]

print(result)