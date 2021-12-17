# 백준 23040 누텔라 트리 (Easy)
# Baekjoon 23040

# Created by sw0817 on 2021. 12. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/23040

import heapq

N = int(input())
heap = []
for _ in range(N):
    nums = list(map(int, input().split()))
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])