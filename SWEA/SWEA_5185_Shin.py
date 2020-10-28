# SWEA 5185 이진수
# SWEA 5185

# Created by sw0817 on 2020. 10. 28..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    N, text = map(str, input().split())
    binary = ''
    for i in range(int(N)):
        if ord(text[i]) >= 65:
            num = ord(text[i]) - 55
        else:
            num = int(text[i])

        a = 3
        while a >= 0:
            if num >= 2 ** a:
                binary += '1'
                num -= 2 ** a
            else:
                binary += '0'
            a -= 1

    print('#{} {}'.format(tc, binary))