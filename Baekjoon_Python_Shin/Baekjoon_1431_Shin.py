# 백준 1431 시리얼 번호
# Baekjoon 1431

# Created by sw0817 on 2022. 11. 10..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1431

N = int(input())
serial = []
for _ in range(N):
    cur = []
    se = input()
    cur.append(len(se))
    _sum = 0
    for n in se:
        try:
            _sum += int(n)
        except:
            continue

    cur.append(_sum)
    cur.append(se)
    serial.append(cur)

serial.sort()
for l, s, se in serial:
    print(se)