# 백준 1086 박성원
# Baekjoon 1086

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1086

from itertools import permutations
import fractions

N = int(input())

t_set = []

for _ in range(N):
    t_set.append(int(input()))

K = int(input())

pers = permutations(t_set, N)
mom = 0
possible = 0

for per in pers:
    mom += 1
    # print(per)
    target = ''

    for num in per:
        target = target + str(num)

    num = int(target)
    if num % K == 0:
        possible += 1

# print(possible)
# print(mom)

a = fractions.Fraction(possible, mom)
possible = a.numerator
mom = a.denominator

print('{}/{}'.format(possible, mom))

# 아직 실패