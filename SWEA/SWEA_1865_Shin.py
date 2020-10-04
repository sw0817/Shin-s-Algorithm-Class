# SWEA 1865 동철이의 일 분배
# SWEA 1865

# Created by sw0817 on 2020. 10. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc&categoryId=AV5LuHfqDz8DFAXc&categoryType=CODE


def perm(n, k, chance):
    global result
    if chance <= result:
        return
    if k == n:
        if chance > result:
            result = chance
            return
    else:
        for i in range(n):
            if V[i] == 0:
                V[i] = 1
                perm(n, k+1, chance * Pies[k][i] / 100)
                V[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    V = [0] * N
    Pies = [list(map(int, input().split())) for _ in range(N)]
    perm(N, 0, 1)
    result *= 100
    print(f'#{tc} {result:.6f}')