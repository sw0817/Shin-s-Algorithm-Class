# SWEA 2806 N-Queen
# SWEA 2806

# Created by sw0817 on 2020. 09. 21..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE


def check(i):
    for j in range(i):
        if G[i] == G[j] or abs(G[i] - G[j]) == i - j:
            return False
    return True


def NQueen(i):
    if i == N:
        global result
        result += 1
    else:
        for j in range(N):
            G[i] = j
            if check(i):
                NQueen(i + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [-1] * N
    result = 0
    NQueen(0)
    print('#{} {}'.format(tc, result))