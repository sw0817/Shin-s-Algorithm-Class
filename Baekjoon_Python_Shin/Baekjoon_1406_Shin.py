# 백준 1406 에디터
# Baekjoon 1406

# Created by sw0817 on 2022. 03. 19..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1406

initial = input()
M = int(input())
left = []
right = []
for w in initial:
    left.append(w)

for _ in range(M):
    a = input()
    if 1 < len(a):
        left.append(a[-1])
    elif a == 'L' and left:
        right.append(left.pop())
    elif a == 'D' and right:
        left.append(right.pop())
    elif a == 'B' and left:
        left.pop()

print("".join(left) + "".join(right)[::-1])