# SWEA 1979 어디에 단어가 들어갈 수 있을까
# SWEA 1979

# Created by sw0817 on 2020. 09. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if G[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    for i in range(N):
        cnt = 0
        for j in range(N):
            if G[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print('#{} {}'.format(tc, result))