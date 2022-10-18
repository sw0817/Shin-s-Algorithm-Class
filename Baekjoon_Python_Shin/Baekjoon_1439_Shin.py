# 백준 1439 뒤집기
# Baekjoon 1439

# Created by sw0817 on 2022. 10. 18..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1439

S = input()
cur = S[0]

cnt = 0
for s in S[1:]:
    if s != cur:
        cur = s
        cnt += 1

print(cnt // 2 + cnt % 2)