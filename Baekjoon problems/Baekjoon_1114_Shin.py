# 백준 1114 통나무 자르기
# Baekjoon 1114

# Created by sw0817 on 2021. 02. 14..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1114

from itertools import combinations

L, K, C = map(int, input().split())

locate = list(map(int, input().split()))
locate.sort()
initial = min_length = L
if K < C:
    C = K

for comb in combinations(locate, C):
    max_length = 0
    temp = 0
    idx = 0
    while max_length <= min_length and idx < C:
        if max_length < comb[idx] - temp:
            max_length = comb[idx] - temp
        temp = comb[idx]
        idx += 1
    if idx == C and max_length < L - temp:
        max_length = L - temp
    if max_length < min_length:
        min_length = max_length
        initial = comb[0]
    elif max_length == min_length and comb[0] < initial:
        initial = comb[0]

print('{} {}'.format(min_length, initial))