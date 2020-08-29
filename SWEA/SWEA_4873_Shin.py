# SWEA 4873 반복문자 지우기
# SWEA 4873

# Created by sw0817 on 2020. 08. 29..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    for alp in text:
        if len(stack) == 0:
            stack.append(alp)
        else:
            if alp == stack[-1]:
                stack.pop()
            else:
                stack.append(alp)

    print('#{} {}'.format(tc, len(stack)))