# SWEA 1220 Magnetic
# SWEA 1220

# Created by sw0817 on 2020. 09. 20..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE


for tc in range(1, 11):
    N = int(input())   # 1은 N극 2는 S극 위가 N
    G = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        check = []
        for j in range(N):
            if G[j][i] != 0:
                check.append(G[j][i])
        while check[-1] == 1:
            check.pop(-1)
        while check[0] == 2:
            check.pop(0)
        check_num = 1
        for k in check:
            if k != check_num:
                check_num = k
                if k == 2:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))