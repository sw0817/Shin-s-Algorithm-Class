# SWEA 6959 이상한 나라의 덧셈게임
# SWEA 6959

# Created by sw0817 on 2020. 08. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWjlH0k63joDFAVT&categoryId=AWjlH0k63joDFAVT&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N = input()
    num = 0
    for i in range(len(N)):
        num += int(N[i])

    if int(N) < 10:
        print('#{} B'.format(tc))
    else:
        cnt = 0
        while num >= 10:
            cnt += 1
            num -= 9

        if (len(N) + cnt) % 2 == 1:
            print('#{} B'.format(tc))
        else:
            print('#{} A'.format(tc))