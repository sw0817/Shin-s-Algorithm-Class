# 백준 2015 수들의 합 4
# Baekjoon 2015

# Created by sw0817 on 2022. 10. 06..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2015

N, K = map(int, input().split())
nums = list(map(int, input().split()))
vals = dict()
vals[0] = 1
cur = 0
ret = 0

for n in nums:
    cur += n
    if cur - K in vals:
        ret += vals[cur - K]

    if cur in vals:
        vals[cur] += 1
    else:
        vals[cur] = 1

print(ret)