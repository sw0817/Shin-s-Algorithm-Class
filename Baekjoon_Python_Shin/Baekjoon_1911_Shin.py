# 백준 1911 흙길 보수하기
# Baekjoon 1911

# Created by sw0817 on 2022. 01. 22..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1911

N, L = map(int, input().split())
cistern = []
for _ in range(N):
    cistern.append(list(map(int, input().split())))

cistern.sort()
idx = 0
cnt = 0

for i in range(N):
    s, e = cistern[i]
    if e <= idx:
        continue
    if idx < s:
        idx = s
    r = e - idx
    c = int(r / L)
    if c < r / L:
        c += 1

    cnt += c
    idx += c * L

print(cnt)