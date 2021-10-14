# 백준 1079 마피아
# Baekjoon 1079

# Created by sw0817 on 2021. 10. 14..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1079

# 밤 횟수, 죽은 놈
def simul(cnt, idx):
    global result
    if result == N // 2:
        return
    if cnt == N // 2:
        result = cnt
        return

    qq = -999999
    n_idx = idx
    for i in range(N):
        if not dead[i]:
            quo[i] += R[idx][i]
            if qq < quo[i]:
                qq = quo[i]
                n_idx = i

    if n_idx == E:
        result = max(result, cnt)
        for i in range(N):
            if not dead[i]:
                quo[i] -= R[idx][i]
        return

    dead[n_idx] = 1
    for i in range(N):
        if not dead[i] and not i == E:
            dead[i] = 1
            simul(cnt+1, i)
            dead[i] = 0

    dead[n_idx] = 0
    for i in range(N):
        if not dead[i]:
            quo[i] -= R[idx][i]


N = int(input())
quo = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
E = int(input())

result = 0
dead = [0] * N

if N % 2:
    idx = 0
    q = 0
    for i in range(N):
        if q < quo[i]:
            q = quo[i]
            idx = i
    dead[idx] = 1
    if idx == E:
        print(0)
    else:
        for i in range(N):
            if not dead[i] and not i == E:
                dead[i] = 1
                simul(1, i)
                dead[i] = 0
        print(result)
else:
    for i in range(N):
        if not i == E:
            dead[i] = 1
            simul(1, i)
            dead[i] = 0
    print(result)