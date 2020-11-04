# SWEA 5202 화물 도크
# SWEA 5202

# Created by sw0817 on 2020. 11. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def check():
    global result
    for i in range(N):
        if result == N:
            return
        cnt = 1
        a = i
        e = se_list[a][1]
        while cnt < N and a < N:
            con = True
            for j in range(a+1, N):
                s = se_list[j][0]
                if s >= e:
                    con = False
                    cnt += 1
                    a = j
                    e = se_list[a][1]
                    break
            if con:
                 break
        if cnt > result:
            result = cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    se_list = []
    for _ in range(N):
        s, e = map(int, input().split())
        se_list.append((s,e))
    se_list.sort(key= lambda x : x[1])
    result = 0
    check()
    print('#{} {}'.format(tc, result))