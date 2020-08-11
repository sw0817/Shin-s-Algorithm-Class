# SWEA 4864 문자열 비교
# SWEA 4864

# Created by sw0817 on 2020. 08. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def str_test(list2, list1):
    for i in range(len(list1)-len(list2)+1):
        result = 0
        if list1[i] == list2[0]:
            for j in range(len(list2)):
                if list1[i + j] != list2[j]:
                    break
                else:
                    result += 1
        if result == len(list2):
            return 1
    return 0

T = int(input())

for tc in range(1, T+1):
    N = list(input())
    M = list(input())

    print('#{} {}'.format(tc, str_test(N, M)))