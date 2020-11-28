# SWEA 10200 구독자 전쟁
# SWEA 10200

# Created by sw0817 on 2020. 11. 28..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXMCXV_qVgkDFAWv&categoryId=AXMCXV_qVgkDFAWv&categoryType=CODE

T = int(input())

for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    if A >= B:
        big = B
    else:
        big = A

    hap = A + B
    if N < hap:
        small = hap - N
    else:
        small = 0

    print('#{} {} {}'.format(tc, big, small))