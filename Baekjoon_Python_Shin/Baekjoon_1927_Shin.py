# 백준 1927 최소 힙
# Baekjoon 1927

# Created by sw0817 on 2020. 10. 14..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1927


import sys
import heapq


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)