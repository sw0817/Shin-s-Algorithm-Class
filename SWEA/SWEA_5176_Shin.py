# SWEA 5176 이진탐색
# SWEA 5176

# Created by sw0817 on 2020. 10. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def add(n):
    global number
    if n <= N:
        add(n*2)
        tree[n] = number
        number += 1
        add(n*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    number = 1
    add(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))