# SWEA 1244 최대 상금
# SWEA 1244

# Created by sw0817 on 2020. 11. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE


from copy import deepcopy


def same_num():
    for i in range(length):
        for j in range(i + 1, length):
            if num_list[i] == num_list[j]:
                return True


T = int(input())
for tc in range(1, T + 1):
    num, N = map(str, input().split())
    length = len(num)
    num_list = list(map(int, num))
    final_check = deepcopy(num_list)
    num_list2 = sorted(num_list, reverse=True)
    visited = [0] * 10
    result = 0
    M = int(N)
    while M > 0:
        for i in range(length):
            if num_list[i] == num_list2[i]:
                continue
            else:
                if M == 0:
                    break
                for j in range(length - 1, -1, -1):
                    if num_list[j] == num_list2[i]:
                        visited[num_list2[i]] += 1
                        M -= 1
                        num_list[i], num_list[j] = num_list[j], num_list[i]
                        break
        break

    for i in range(10):
        if visited[i] >= 2:
            sorting = []
            for j in range(length):
                if final_check[j] == i and final_check[j] != num_list[j]:
                    sorting.append((num_list[j], j))
            sorting2 = sorted(sorting, reverse=True)
            for j in range(len(sorting)):
                num_list[sorting[j][1]] = sorting2[j][0]

    if M % 2 == 0:
        for i in range(length):
            result += num_list[i] * (10 ** (length - 1 - i))

    else:
        if same_num():
            for i in range(length):
                result += num_list[i] * (10 ** (length - 1 - i))
        else:
            for i in range(length):
                result += num_list[i] * (10 ** (length - 1 - i))

    print('#{} {}'.format(tc, result))