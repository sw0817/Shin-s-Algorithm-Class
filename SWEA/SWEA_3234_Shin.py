# SWEA 3234 준환이의 양팔저울
# SWEA 3234

# Created by sw0817 on 2021. 01. 07..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw&categoryId=AWAe7XSKfUUDFAUw&categoryType=CODE

factorial = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def check(n, left, right):
    global result, total

    if n == N:
        result += 1
        return
    if total-left <= left:
        result += 2 ** (N-n) * factorial[N-n]
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            check(n+1, left+weights[i], right)
            if right+weights[i] <= left:
                check(n+1, left, right+weights[i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    total = sum(weights)
    result = 0
    visited = [0] * N
    check(0, 0, 0)

    print('#{} {}'.format(tc, result))