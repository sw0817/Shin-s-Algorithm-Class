# 백준 2790 F7
# Baekjoon 2790

# Created by sw0817 on 2022. 04. 06..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2790

N = int(input())
score = [int(input()) for _ in range(N)]
score = sorted(score)
first = 0
for i in range(N):
    score[i] += N - i
    first = max(first, score[i])

result = 0
for i in range(N-1):
    if first <= score[i]:
        result += 1
    score[i+1] += i + 1

if first < score[-1]:
    result += 1

print(result)
