# SWEA 4861 회문
# SWEA 4861

# Created by sw0817 on 2020. 08. 14..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def pal(a, b): # list, M
    for i in range(2, len(a)):
        for j in range(len(a)-b+1):
            cnt = 0
            if a[i][j] == a[i][j+b-1]:
                for k in range(b):
                    if a[i][j+k] != a[i][j+b-1-k]:
                        break
                    else:
                        cnt += 1
                if cnt == b:
                    result = ''
                    for l in range(b):
                        result += a[i][j+l]
                    return result

    for i in range(len(a)-b+1):
        for j in range(len(a)):
            cnt = 0
            if a[i][j] == a[i+b-1][j]:
                for k in range(b):
                    if a[i+k][j] != a[i+b-1-k][j]:
                        break
                    else:
                        cnt += 1
                if cnt == b:
                    result = ''
                    for l in range(b):
                        result += a[i+l][j]
                    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = []
    for i in range(N):
        words.append(list(input()))

    print('#{} {}'.format(tc, pal(words, M)))