# SWEA 5987 달리기
# SWEA 5987

# Created by sw0817 on 2020. 08. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWaJ4g86WA4DFAUQ&categoryId=AWaJ4g86WA4DFAUQ&categoryType=CODE


T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    inf_list = []
    for j in range(M):
        inf_list.append(list(map(int, input().split())))
        # inf_list[x][y]

