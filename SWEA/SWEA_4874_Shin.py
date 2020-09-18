# SWEA 4874 Forth
# SWEA 4874

# Created by sw0817 on 2020. 09. 18..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    operator = ['+', '-', '*', '/']
    dot = ['.']
    mod = list(input().split())
    cnt = 0
    for i in range(len(mod)):
        if mod[i] not in operator and mod[i] not in dot:
            mod[i] = int(mod[i])
            cnt += 1
    A = 0
    if cnt != len(mod) - cnt:
        print('#{} error'.format(tc))
    else:
        while len(mod) != 2:
            if mod[0] in operator or mod[1] in operator:
                A = 1
                break
            for i in range(len(mod)):
                if mod[i] in operator:
                    if mod[i] == '+':
                        mod[i] = mod[i-2] + mod[i-1]
                    elif mod[i] == '-':
                        mod[i] = mod[i-2] - mod[i-1]
                    elif mod[i] == '*':
                        mod[i] = mod[i-2] * mod[i-1]
                    elif mod[i] == '/':
                        mod[i] = (mod[i-2] // mod[i-1])
                    mod.pop(i-2)
                    mod.pop(i-2)
                    break

        if A == 1:
            print('#{} error'.format(tc))
        else:
            print('#{} {}'.format(tc, mod[0]))