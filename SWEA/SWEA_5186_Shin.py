# SWEA 5186 이진수2
# SWEA 5186

# Created by sw0817 on 2020. 10. 29..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    a = 1
    while a < 13:
        if N >= 2 ** (-a):
            result += '1'
            N -= 2 ** (-a)
        elif N > 0:
            result += '0'
        if N == 0:
            break
        a += 1
        if a == 13:
            result = 'overflow'
            break
    print('#{} {}'.format(tc, result))