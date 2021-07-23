# 백준 1662 압축
# Baekjoon 1662

# Created by sw0817 on 2021. 07. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1662

from collections import deque

S = input()
stack = deque()
l = 0
temp = 0
for s in S:
    if s == '(':
        stack.append((temp, l-1))
        l = 0
    elif s == ')':
        num, pre = stack.pop()
        l = num * l + pre
    else:
        l += 1
        temp = int(s)
    # print(l)
    # print(stack)
    # print()

print(l)