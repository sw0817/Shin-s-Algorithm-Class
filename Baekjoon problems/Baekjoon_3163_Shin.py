# 백준 3163 떨어지는 개미
# Baekjoon 3163

# Created by sw0817 on 2021. 09. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3163

T = int(input())
for tc in range(T):
    N, L, k = map(int, input().split())
    ants = []
    left_time = []
    right_time = []
    left = 0
    for i in range(1, N+1):
        p, a = map(int, input().split())
        if a < 0:
            left += 1
            left_time.append(p)
        else:
            right_time.append(L-p)
        ants.append(a)

    left_time.sort()
    right_time.sort()
    l_idx = 0
    r_idx = 0
    cnt = 0

    while cnt < k-1 and l_idx < left or cnt < k-1 and r_idx < N - left:
        if l_idx < left and r_idx < N - left:
            if left_time[l_idx] < right_time[r_idx]:
                l_idx += 1
            elif left_time[l_idx] > right_time[r_idx]:
                r_idx += 1
            else:
                if abs(ants[l_idx]) < ants[N-1-r_idx]:
                    l_idx += 1
                else:
                    r_idx += 1
            cnt += 1
        elif l_idx < left:
            l_idx += k - cnt - 1
            cnt = k - 1
        else:
            r_idx += k - cnt - 1
            cnt = k - 1

    if l_idx < left and r_idx < N - left:
        if left_time[l_idx] < right_time[r_idx]:
            print(ants[l_idx])
        elif left_time[l_idx] > right_time[r_idx]:
            print(ants[N-1-r_idx])
        else:
            if abs(ants[l_idx]) < ants[N-1-r_idx]:
                print(ants[l_idx])
            else:
                print(ants[N-1-r_idx])

    elif l_idx < left:
        print(ants[l_idx])
    else:
        print(ants[N-1-r_idx])