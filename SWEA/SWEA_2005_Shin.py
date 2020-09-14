# SWEA 2005 파스칼의 삼각형
# SWEA 2005

# Created by sw0817 on 2020. 09. 14..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []
    for i in range(N):
        con = []
        for j in range(i+1):
            if j == 0 or j == i:
                con.append(1)
            else:
                con.append(result[i-1][j-1]+result[i-1][j])
        result.append(con)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print(result[i][j], end=' ')
        print()