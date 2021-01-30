# SWEA 3142 영준이와 신비한 뿔의 숲
# SWEA 3142

# Created by sw0817 on 2021. 01. 31..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV_6xWk6sbADFAWS&categoryId=AV_6xWk6sbADFAWS&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

T = int(input())

for tc in range(1, T+1):

    # 뿔의 개수 N, 짐승의 수 M
    N, M = map(int, input().split())

    print("#{} {} {}".format(tc, N-(2*(N-M)), N-M))