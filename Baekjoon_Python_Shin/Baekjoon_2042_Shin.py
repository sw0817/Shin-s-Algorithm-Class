# 백준 2042 구간 합 구하기
# Baekjoon 2042

# Created by sw0817 on 2020. 10. 17..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2042


from collections import deque


N, M, K = map(int, input().split())
nums = deque()
for _ in range(N):
    nums.append(int(input()))
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        nums[b-1] = c
    else:
        cnt = 0
        for i in range(c-b+1):
            cnt += nums[i+b-1]

        print(cnt)
