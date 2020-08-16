# SWEA 4865 글자수
# SWEA 4865

# Created by sw0817 on 2020. 08. 16..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = list(input())
    str_list = []
    max_cnt = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        if cnt >= max_cnt:
            max_cnt = cnt
    print('#{} {}'.format(tc, max_cnt))
