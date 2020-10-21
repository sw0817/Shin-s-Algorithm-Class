# SWEA 1952 수영장
# SWEA 1952

# Created by sw0817 on 2020. 10. 21..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq&categoryType=CODE


def min_sum(m, s):
    global result
    if m > 11:
        if result > s:
            result = s
            return
    else:
        min_sum(m+1, s+dates[m])
        min_sum(m+3, s+fares[2])


T = int(input())
for tc in range(1, T+1):
    fares = list(map(int, input().split()))
    dates = list(map(int, input().split()))

    result = fares[3]

    for i in range(12):
        if dates[i] * fares[0] <= fares[1]:
            dates[i] = dates[i] * fares[0]
        else:
            dates[i] = fares[1]

    for i in range(12):
        if dates[i] > 0:
            min_sum(i, 0)
            break

    print('#{} {}'.format(tc, result))

