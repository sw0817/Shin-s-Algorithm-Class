# SWEA 4881 배열 최소 합
# SWEA 4881

# Created by sw0817 on 2020. 09. 23..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def check(i):
    for j in range(i):
        if V[i] == V[j]:
            return False
    return True

def arr(i, num):
    global result
    if i == N:
        if num < result:
            result = num
        return
    if num >= result:
        return
    else:
        for j in range(N):
            V[i] = j
            if check(i):
                arr(i+1, num + G[i][V[i]])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    result = 9 * (N ** 2)
    V = [-1] * N
    arr(0, 0)
    print('#{} {}'.format(tc, result))