# SWEA 4047 영준이의 카드 카운팅
# SWEA 4047

# Created by sw0817 on 2020. 09. 26..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIsY84KEPMDFAWN&categoryId=AWIsY84KEPMDFAWN&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    text = list(input())
    S = []
    H = []
    D = []
    C = []
    ERROR = 0
    while len(text) != 0:
        dummy = ''
        for _ in range(3):
            dummy = text[-1] + dummy
            text.pop(-1)
        if dummy[0] == 'S':
            if dummy in S:
                ERROR = 1
                break
            S.append(dummy)
        elif dummy[0] == 'H':
            if dummy in H:
                ERROR = 1
                break
            H.append(dummy)
        elif dummy[0] == 'D':
            if dummy in D:
                ERROR = 1
                break
            D.append(dummy)
        elif dummy[0] == 'C':
            if dummy in C:
                ERROR = 1
                break
            C.append(dummy)

    if ERROR == 1:
        print('#{} ERROR'.format(tc))
    else:
        print('#{} {} {} {} {}'.format(tc, 13-len(S), 13-len(D), 13-len(H), 13-len(C)))