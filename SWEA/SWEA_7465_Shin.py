# SWEA 7465 창용 마을 무리의 개수
# SWEA 7465

# Created by sw0817 on 2020. 08. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU&categoryId=AWngfZVa9XwDFAQU&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(M):
        arr.append(list(map(int, input().split())))


    group = 0
    test_list = []
    for i in range(1, N+1):
        test_list.append(i)

    while test_list != []:
        test_set = set()
        for i in range(M):
            if arr[i][0] == test_list[0] or arr[i][1] == test_list[0]:
                test_set.add(arr[i][0])
                test_set.add(arr[i][1])
            else:
                continue
            for j in range(M):
                if arr[j][0] in test_set or arr[j][1] in test_set:
                    test_set.add(arr[j][0])
                    test_set.add(arr[j][1])
            for k in range(M):
                if arr[k][0] in test_set or arr[k][1] in test_set:
                    test_set.add(arr[k][0])
                    test_set.add(arr[k][1])
            group += 1
            list_set = list(test_set)
            for l in range(len(list_set)):
                test_list.remove(list_set[l])
            break
    print('#{} {}'.format(tc, group))
