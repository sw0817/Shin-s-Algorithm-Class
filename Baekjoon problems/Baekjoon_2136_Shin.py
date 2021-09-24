# 백준 2136 개미
# Baekjoon 2136

# Created by sw0817 on 2021. 09. 24..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2136

N, L = map(int, input().split())
ants = []
left = 0
last = [0, 0]
for i in range(1, N+1):
    t = int(input())
    if t < 0:
        left += 1
        t = abs(t)
        if last[0] < t:
            last[0] = t
            last[1] = 0
        ants.append((t, i))
    else:
        if last[0] < L - t:
            last[0] = L - t
            last[1] = 1
        ants.append((t, i))

ants = sorted(ants)

if last[1]:
    print(ants[left][1], last[0])
else:
    print(ants[left-1][1], last[0])