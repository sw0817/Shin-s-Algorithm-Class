# SWEA 10507 영어 공부
# SWEA 10507

# Created by sw0817 on 2020. 10. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXNQOb3avD0DFAXS&categoryId=AXNQOb3avD0DFAXS&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    n, p = map(int, input().split())
    real_study = list(map(int, input().split()))
    between_days = []
    for i in range(n-1):
        between_days.append(real_study[i+1] - real_study[i])
    max_days = p+1
    idx = 0
    continuous = 1
    temp = p
    temp_idx = idx
    temp_temp = 0

    while idx < n-1:
        if between_days[idx] - 1 <= temp:
            if temp == p and between_days[idx] > 1:
                temp_idx = idx
            continuous += between_days[idx]
            temp -= between_days[idx] - 1
            if continuous + temp > max_days:
                max_days = continuous + temp
        else:
            if temp_idx != 0:
                idx = temp_idx
                temp_idx = 0
            continuous = 1
            temp = p

        idx += 1

    print('#{} {}'.format(tc, max_days))