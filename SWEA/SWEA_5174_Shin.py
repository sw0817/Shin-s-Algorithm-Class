# SWEA 5174 subtree
# SWEA 5174

# Created by sw0817 on 2020. 10. 09..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def cnt(n):
    global result
    for son in tree[n]:
        if son != 0:
            result += 1
            cnt(son)


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0] * 2 for _ in range(E+2)]
    Es = list(map(int, input().split()))
    for i in range(E):
        if tree[Es[i*2]][0] == 0:
            tree[Es[i*2]][0] = Es[i*2+1]
        else:
            tree[Es[i*2]][1] = Es[i*2+1]
    result = 1
    cnt(N)
    print('#{} {}'.format(tc, result))