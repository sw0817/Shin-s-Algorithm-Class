# 백준 17143 낚시왕
# Baekjoon 17143

# Created by sw0817 on 2021. 02. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17143

move = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]

R, C, M = map(int, input().split())
sharks = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d == 1 or 2:
        s = s % (2*(R-1))
    else:
        s = s % (2*(C-1))
    sharks.append((r, c, s, d, z))

step = 0
result = 0

while step < C and len(sharks):
    sharks.sort()
    step += 1
    for shark in sharks:
        if shark[0] == step:
            result += shark[4]
            sharks.remove(shark)
            break
    shark_rc = []
    idx = 0
    while idx < len(sharks) - 1:
        r, c, s, d, z = sharks[idx]
        if d == 1:
            if s <= r:
                r -= s
            else:
                if s-r <= R-1:
                    r = s-r
                else:
                    r = 2*(R-1) - (s-r)
        elif d == 2:
            if r+s <= (R-1):
                r += s
            else:
                if 2*(R-1) < r+s:
                    r = r+s - (2*(R-1))
                else:
                    r = (2*(R-1)) - (r+s)
        elif d == 3:
            if s <= c:
                c -= s
            else:
                if s - c <= C - 1:
                    c = s - c
                else:
                    c = 2 * (C - 1) - (s - c)
        else:
            if c+s <= (C-1):
                c += s
            else:
                if 2*(C-1) < c+s:
                    c = c+s - (2*(C-1))
                else:
                    c = (2*(C-1)) - (c+s)

        if not (r, c) in shark_rc:
            shark_rc.append((r, c))
        else:
            for i in range(len(shark_rc)):
                if shark_rc[i] == (r, c):
