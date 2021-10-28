# 백준 1092 배
# Baekjoon 1092

# Created by sw0817 on 2021. 10. 28..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1092

import math

N = int(input())
crane = list(map(int, input().split()))
crane.sort()
cnts = [0] * N
M = int(input())
boxes = list(map(int, input().split()))
boxes.sort()

if max(crane) < max(boxes):
    print(-1)
else:
    idx = 0
    for i in range(N):
        while idx < M:
            if boxes[idx] <= crane[i]:
                idx += 1
            else:
                break
        cnts[i] = idx

    cnts.sort(reverse=True)
    cnt = 0
    days = 0
    for i in range(N-1, -1, -1):
        if M <= cnt:
            break
        if cnts[i] <= days:
            continue
        if cnt + (cnts[i]-days) * (i+1) <= M:
            cnt += (cnts[i]-days) * (i+1)
            days = cnts[i]
        else:
            days += math.ceil((M - cnt) / (i+1))
            break

    print(days)

# 미완