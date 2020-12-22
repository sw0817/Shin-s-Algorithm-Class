# 백준 2437 저울
# Baekjoon 2437

# Created by sw0817 on 2020. 12. 22..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2437

N = int(input())
weights = list(map(int, input().split()))

weights.sort()

num = 1
for i in range(N):
    if num < weights[i]:
        break
    num += weights[i]

print(num)