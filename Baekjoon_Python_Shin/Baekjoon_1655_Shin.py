# 백준 1655 가운데를 말해요
# Baekjoon 1655

# Created by sw0817 on 2021. 02. 15..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1655

from sys import stdin
import heapq

left, right = [], []
N = int(stdin.readline())
for _ in range(N):
    num = int(stdin.readline())
    # max_heap 조건
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    # min_heap
    else:
        heapq.heappush(right, (num, num))

    # left보다 right가 커야한다.
    if right and left[0][1] > right[0][1]:
        current_left = heapq.heappop(left)[1]
        current_right = heapq.heappop(right)[1]
        heapq.heappush(right, (current_left, current_left))
        heapq.heappush(left, (-current_right, current_right))

    print(left[0][1])