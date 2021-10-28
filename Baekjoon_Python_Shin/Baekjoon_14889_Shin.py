# 백준 14889 스타트와 링크
# Baekjoon 14889

# Created by sw0817 on 2021. 10. 29..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14889

import math
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
c = [i for i in range(N)]
result = math.inf
comb_list = list(combinations(c, N // 2))
l = len(comb_list)
for i in range(l // 2):
    A = comb_list[i]
    B = comb_list[l-i-1]
    a_score = 0
    b_score = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            a_score += arr[A[i]][A[j]] + arr[A[j]][A[i]]
            b_score += arr[B[i]][B[j]] + arr[B[j]][B[i]]
    result = min(result, abs(a_score - b_score))

print(result)