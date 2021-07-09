# 백준 1562 계단 수
# Baekjoon 1562

# Created by sw0817 on 2021. 07. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1562

from collections import deque

N = int(input())
queue = deque(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
cnt = 0
result = 0
while queue:
    cnt += 1
    if cnt == N:
        for _ in range(len(queue)):
            num = queue.popleft()
            if len(set(list(num))) == 10:
                result += 1
    for _ in range(len(queue)):
        num = queue.popleft()
        l = len(set(list(num)))
        if l == 10:
            result += 1
            continue
        if l + N - cnt < 10:
            continue
        n = int(num[-1])
        if n == 0:
            queue.append(num + '1')
        elif n == 9:
            queue.append(num + '8')
        else:
            queue.append(num + str(n-1))
            queue.append(num + str(n+1))

print(result % 1000000000)
# 아직 메모리 초과 못 잡음