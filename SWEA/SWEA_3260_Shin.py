# SWEA 3260 두 수의 덧셈
# SWEA 3260

# Created by sw0817 on 2021. 01. 31..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWBC1lOad9IDFAWr&categoryId=AWBC1lOad9IDFAWr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    print('#{} {}'.format(tc, a+b))