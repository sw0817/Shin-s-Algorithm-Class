# 백준 2014 소수의 곱
# Baekjoon 2014

# Created by sw0817 on 2021. 12. 10..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2014

import heapq

K, N = map(int, input().split())
nums = list(map(int, input().split()))
queue = []
for num in nums:
    heapq.heappush(queue, num)

result = 0
for i in range(N):
    result = heapq.heappop(queue)
    for num in nums:
        n = result * num
        heapq.heappush(queue, n)
        if not result % num:
            break

print(result)