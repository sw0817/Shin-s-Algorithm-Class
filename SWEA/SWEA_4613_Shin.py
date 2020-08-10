# SWEA 4613 러시아 국기 같은 깃발
# SWEA 4613

# Created by sw0817 on 2020. 08. 10..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj&categoryId=AWQl9TIK8qoDFAXj&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = N*M
    ini_list = []
    for i in range(N):
        ini_list.append(list(input()))

    cnt = 0

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(i+1):
                for l in range(M):
                    if ini_list[k][l] != 'W':
                        cnt += 1
            for k in range(i+1, j+1):
                for l in range(M):
                    if ini_list[k][l] != 'B':
                        cnt += 1
            for k in range(j+1, N):
                for l in range(M):
                    if ini_list[k][l] != 'R':
                        cnt += 1
            if cnt <= result:
                result = cnt
            cnt = 0
    print('#{} {}'.format(tc, result))