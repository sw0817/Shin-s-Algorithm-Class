# 백준 2014 소수의 곱
# Baekjoon 2014

# Created by sw0817 on 2021. 12. 10..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2014

import heapq

K, N = map(int, input().split())
nums = list(map(int, input().split()))
queue = []
# num 도 N 번째 소수에 포함
for num in nums:
    heapq.heappush(queue, num)

result = 0
# N 번 소수를 뽑아낸다.
for i in range(N):
    result = heapq.heappop(queue)
    # 주어진 기준 소수를 곱해서 새로운 소수 생성
    for num in nums:
        n = result * num
        heapq.heappush(queue, n)
        # 기준 소수의 곱이 아니라는 것은,
        # 다음 소수의 곱으로 만들어진 수가
        # 현재 result 와의 곱을 만들어내므로 중복이 발생함
        if not result % num:
            break

print(result)