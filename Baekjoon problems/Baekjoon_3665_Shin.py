# 백준 3665 최종 순위
# Baekjoon 3665

# Created by sw0817 on 2020. 01. 01..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3665

from _collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    last = list(map(int, input().split()))
    M = int(input())
    this = [[] for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            this[last[i]-1].append(last[j]-1)

    for i in range(M):
        check = True
        high, low = map(int, input().split())
        for i in this[high-1]:
            if i == low-1:
                this[high-1].remove(low-1)
                this[low-1].append(high-1)
                check = False
        if check:
            this[low-1].remove(high-1)
            this[high-1].append(low-1)

    queue = deque()

    result = 0
    final_list = []

    len_list = [0] * N
    for array in this:
        for number in array:
            len_list[number] += 1

    for i in range(N):
        if len_list[i] == 0:
            queue.append(i)

    if not queue:
        result = 1

    while queue:
        if 2 < len(queue):
            result = 1
            break

        num = queue.popleft()
        final_list.append(num+1)

        for i in this[num]:
            len_list[i] -= 1
            if len_list[i] == 0:
                queue.append(i)
            elif len_list[i] < 0:
                result = 1
                break

    if 0 < result or len(final_list) < N:
        print('IMPOSSIBLE')
    else:
        print(*final_list)