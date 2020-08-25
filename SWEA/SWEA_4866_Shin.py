# SWEA 4866 괄호검사
# SWEA 4866

# Created by sw0817 on 2020. 08. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def check(st):
    for i in range(len(st)):
        if st[i] == '(':
            stack.append(st[i])
        elif st[i] == ')':

            if len(stack) == 0 or stack[-1] != '(':
                return 0
            else:
                stack.pop()

        elif st[i] == '{':
            stack.append(st[i])
        elif st[i] == '}':

            if len(stack) == 0 or stack[-1] != '{':
                return 0
            else:
                stack.pop()

    if stack:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    stack = []
    st = input()
    print('#{} {}'.format(tc, check(st)))
