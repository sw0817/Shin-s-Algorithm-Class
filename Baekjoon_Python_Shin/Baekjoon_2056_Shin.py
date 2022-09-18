# 백준 2056 작업
# Baekjoon 2056

# Created by sw0817 on 2022. 09. 18..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2056

M = int(input())
fs = dict()
ts = [0] * (M+1)
for i in range(1, M+1):
    info = list(map(int, input().split()))
    ts[i] = info[0]
    if info[1]:
        for j in info[2:]:
            if i in fs:
                fs[i].append(j)
            else:
                fs[i] = [j]

for i in range(1, M+1):
    if i in fs:
        t = 0
        for j in fs[i]:
            t = max(t, ts[j])
        ts[i] += t

print(max(ts))