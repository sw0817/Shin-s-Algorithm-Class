# 백준 17143 낚시왕
# Baekjoon 17143

# Created by sw0817 on 2021. 02. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17143

R, C, M = map(int, input().split())
sharks = []

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r-1, c-1, s, d, z))

step = -1
result = 0

while step < C and len(sharks):
    sharks.sort()
    step += 1
    for shark in sharks:
        if shark[1] == step:
            result += shark[4]
            sharks.remove(shark)
            break

    shark_rc = []
    idx = 0
    while idx < len(sharks):
        r, c, s, d, z = sharks[idx]
        if d == 1:
            if ((R-1-r+s) // (R-1)) % 2:
                d = 2
                r = ((R-1-r+s) % (R-1))
            else:
                r = (R-1) - ((R-1-r+s) % (R-1))

        elif d == 2:
            if ((r+s) // (R-1)) % 2:
                d = 1
                r = (R-1) - ((r+s) % (R-1))
            else:
                r = ((r+s) % (R-1))

        elif d == 3:
            if ((c+s) // (C-1)) % 2:
                d = 4
                c = (C-1) - ((c+s) % (C-1))
            else:
                c = ((c+s) % (C-1))

        else:
            if ((C-1-c+s) // (C-1)) % 2:
                d = 3
                c = ((C-1-c+s) % (C-1))
            else:
                c = (C-1) - ((C-1-c+s) % (C-1))

        if not (r, c) in shark_rc:
            shark_rc.append((r, c))
            sharks[idx] = (r, c, s, d, z)
            idx += 1
        else:
            for i in range(len(shark_rc)):
                if shark_rc[i] == (r, c):
                    if sharks[i][4] < sharks[idx][4]:
                        del sharks[i]
                        del shark_rc[i]
                        shark_rc.append((r, c))
                    else:
                        del sharks[idx]
                    break

print(result)