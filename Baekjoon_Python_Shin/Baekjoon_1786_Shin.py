# 백준 1786 찾기
# Baekjoon 1786

# Created by sw0817 on 2020. 12. 13..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1786

T = input()
P = input()

kmpTable = [0] * len(P)

i = 0

for j in range(1, len(P)):
    while i > 0 and P[j] != P[i]:
        i = kmpTable[i-1]

    if P[j] == P[i]:
        i += 1
        kmpTable[j] = i

count = 0
result = []

i = 0

for j in range(len(T)):
    while i > 0 and T[j] != P[i]:
        i = kmpTable[i-1]

    if T[j] == P[i]:
        if i == len(P) - 1:
            count += 1
            result.append(j - len(P) + 2)
            i = kmpTable[i]

        else:
            i += 1

print(count)
print(*result)