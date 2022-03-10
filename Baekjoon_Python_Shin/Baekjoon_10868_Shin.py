# 백준 10868 최솟값
# Baekjoon 10868

# Created by sw0817 on 2022. 03. 10..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10868

from sys import stdin
from math import ceil, log

def makeMin(l, r, n_l, n_r, num):
    if l > n_r or r < n_l:
        return inf
    if l <= n_l and r >= n_r:
        return arr[num]
    mid = (n_l + n_r) // 2
    return min(makeMin(l, r, n_l, mid, num * 2), makeMin(l, r, mid+1, n_r, num * 2 + 1))


inf = 1000000000
N, M = map(int, stdin.readline().split())
size = 2 ** ceil(log(N, 2))
max_size = size * 2

arr = [inf] * max_size
for i in range(N):
    arr[size+i] = int(stdin.readline())

for i in range(size - 1, 0, -1):
    arr[i] = min(arr[i*2], arr[i*2+1])

for _ in range(M):
    s, e = map(int, stdin.readline().split())
    print(makeMin(s-1, e-1, 0, size-1, 1))