# SWEA 6019 기차 사이의 파리
# SWEA 6019

# Created by sw0817 on 2020. 08. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWajaTmaZw4DFAWM&categoryId=AWajaTmaZw4DFAWM&categoryType=CODE


T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    num = 1
    num2 = 1
    for i in range(M):
        num = num * i
    for j in range(N-M):
        num2 = num2 * M
    result = num * num2 % 1000000007
    print('#{} {}'.format(tc, result))
