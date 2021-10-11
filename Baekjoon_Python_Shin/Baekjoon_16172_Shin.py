# 백준 16172 나는 친구가 적다 (Large)
# Baekjoon 16172

# Created by sw0817 on 2021. 10. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/16172

S = input()
new_S = ''
for s in S:
    if not 48 <= ord(s) < 58:
        new_S += s
K = input()
l_S = len(new_S)
l_K = len(K)

if l_S < l_K:
    print(0)
else:
    for i in range(l_S - l_K + 1):
        if new_S[i] == K[0]:
            idx = 1
            while idx < l_K and new_S[i+idx] == K[idx]:
                idx += 1
            if idx == l_K:
                print(1)
                break
    else:
        print(0)

## 현재는 시간초과