# 백준 17071 숨바꼭질 5
# Baekjoon 17071

# Created by sw0817 on 2021. 10. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17071

from collections import deque

def solution(N, K):
    queue = deque()
    queue.append(N)
    location = [[0] * 500001 for _ in range(2)]
    location[0][N] = 1
    t = 0
    oe = 0 # Odd, Even

    while queue:
        if 500000 < K:
            break
        if location[oe][K]:
            return t

        oe = 1 - oe
        for _ in range(len(queue)):
            l = queue.popleft()
            for i in (l-1, l+1, l*2):
                if 0 <= i <= 500000 and not location[oe][i]:
                    location[oe][i] = 1
                    queue.append(i)

        t += 1
        K += t

    return -1


N, K = map(int, input().split())
print(solution(N, K))