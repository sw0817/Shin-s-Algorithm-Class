# SWEA 10966 물놀이를 가자
# SWEA 10966

# Created by sw0817 on 2021. 03. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST&categoryId=AXWXMZta-PsDFAST&categoryType=CODE&problemTitle=%EB%AC%BC%EB%86%80%EC%9D%B4&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    print('#{}'.format(test_case), end=' ')

    N, M = map(int, input().split())
    WL_map = []
    for i in range(N):
        WL_map += [input()]

    count = []
    location = []
    for i in range(N):
        count.append([])
        for j in range(M):
            if WL_map[i][j] == 'W':
                count[i] += [0]
                location += [(i, j)]
            else:
                count[i] += [-1]
    loop = 0
    l_num = N * M - len(location)
    loop_num = 1
    while loop < l_num:
        temp = []
        for item in location:
            if item[0] > 0:
                if count[item[0] - 1][item[1]] == -1:
                    loop += 1
                    count[item[0] - 1][item[1]] = loop_num
                    temp += [(item[0] - 1, item[1])]
            if item[0] < N - 1:
                if count[item[0] + 1][item[1]] == -1:
                    loop += 1
                    count[item[0] + 1][item[1]] = loop_num
                    temp += [(item[0] + 1, item[1])]
            if item[1] > 0:
                if count[item[0]][item[1] - 1] == -1:
                    loop += 1
                    count[item[0]][item[1] - 1] = loop_num
                    temp += [(item[0], item[1] - 1)]
            if item[1] < M - 1:
                if count[item[0]][item[1] + 1] == -1:
                    loop += 1
                    count[item[0]][item[1] + 1] = loop_num
                    temp += [(item[0], item[1] + 1)]
        location = temp
        loop_num += 1

    result = 0
    for i in count:
        result += sum(i)
    print(result)