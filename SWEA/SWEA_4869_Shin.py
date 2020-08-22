# SWEA 4869 종이붙이기
# SWEA 4869

# Created by sw0817 on 2020. 08. 22..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return paper(n-1) + 2 * paper(n-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N = 10x
    n = N // 10

    print('#{} {}'.format(tc, paper(n)))