# 백준 23629 이 얼마나 끔찍하고 무시무시한 수식이니
# Baekjoon 23629

# Created by sw0817 on 2022. 01. 03..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/23629

import math

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
names = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

def cal():
    last = ''
    for s in queue:
        last += str(s)

    idx = 0
    l = len(queue)
    cur = 0

    cur += int(queue[idx])
    idx += 1

    while idx < l-1:
        if queue[idx] == '=' or idx == l-2:
            return 'Madness!'

        if idx < l-2:
            if queue[idx+1] in ['x', '/', '+', '-', '=']:
                return 'Madness!'
            if queue[idx] == 'x':
                if queue[idx+1] == '-':
                    if queue[idx+2] in ['x', '/', '+', '-', '=']:
                        return 'Madness!'
                    cur *= -int(queue[idx+2])
                    idx += 3
                else:
                    cur *= int(queue[idx+1])
                    idx += 2
            elif queue[idx] == '/':
                if queue[idx+1] == '-':
                    if queue[idx+2] in ['x', '/', '+', '-', '=']:
                        return 'Madness!'
                    cur /= -int(queue[idx+2])
                    if cur < 0:
                        cur = math.ceil(cur)
                    else:
                        cur = int(cur)
                    idx += 3
                else:
                    cur /= int(queue[idx+1])
                    if cur < 0:
                        cur = math.ceil(cur)
                    else:
                        cur = int(cur)
                    idx += 2
            elif queue[idx] == '-':
                if queue[idx+1] == '-':
                    if queue[idx+2] in ['x', '/', '+', '-', '=']:
                        return 'Madness!'
                    cur -= -int(queue[idx+2])
                    idx += 3
                else:
                    cur -= int(queue[idx+1])
                    idx += 2
            elif queue[idx] == '+':
                if queue[idx+1] == '-':
                    if queue[idx+2] in ['x', '/', '+', '-', '=']:
                        return 'Madness!'
                    cur += -int(queue[idx+2])
                    idx += 3
                else:
                    cur += int(queue[idx+1])
                    idx += 2

    s = str(cur)
    print(last)
    ret = ''
    for i in s:
        if i in numbers:
            ret += names[numbers.index(i)]
        else:
            ret += i
    return ret


info = input()
queue = []
idx = 0
l = len(info)
cur = ''
valid = True
while idx < l:
    s = info[idx]
    if s == 'O':
        if info[idx:idx+3] != names[1]:
            valid = False
            break
        cur += '1'
        idx += 3
        continue
    elif s == 'T':
        if info[idx+1] == 'W':
            if info[idx:idx+3] != names[2]:
                valid = False
                break
            cur += '2'
            idx += 3
            continue
        else:
            if info[idx:idx+5] != names[3]:
                valid = False
                break
            cur += '3'
            idx += 5
            continue
    elif s == 'F':
        if info[idx+1] == 'O':
            if info[idx:idx+4] != names[4]:
                valid = False
                break
            cur += '4'
        else:
            if info[idx:idx+4] != names[5]:
                valid = False
                break
            cur += '5'
        idx += 4
        continue
    elif s == 'S':
        if info[idx+1] == 'I':
            if info[idx:idx+3] != names[6]:
                valid = False
                break
            cur += '6'
            idx += 3
            continue
        else:
            if info[idx:idx+5] != names[7]:
                valid = False
                break
            cur += '7'
            idx += 5
            continue
    elif s == 'E':
        if info[idx:idx+5] != names[8]:
            valid = False
            break
        cur += '8'
        idx += 5
        continue
    elif s == 'N':
        if info[idx:idx+4] != names[9]:
            valid = False
            break
        cur += '9'
        idx += 4
        continue
    elif s == 'Z':
        if info[idx:idx+4] != names[0]:
            valid = False
            break
        cur += '0'
        idx += 4
        continue
    else:
        if s not in ['x', '/', '+', '-', '=']:
            valid = False
            break
        if cur:
            queue.append(cur)
        cur = ''
        queue.append(s)
        idx += 1
        continue

if not valid:
    print('Madness!')
else:
    print(cal())