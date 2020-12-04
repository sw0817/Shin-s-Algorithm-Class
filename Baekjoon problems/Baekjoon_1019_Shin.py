# 백준 1019 책 페이지
# Baekjoon 1019

# Created by sw0817 on 2020. 12. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1019

N = int(input())

nums = [0] * 10

co = 1

while N != 0:
    while N % 10 != 9:
        for i in str(N):
            nums[int(i)] += co
        N -= 1

    if N < 10:
        for i in range(N+1):
            nums[i] += co
        nums[0] -= co
        break

    else:
        for i in range(10):
            nums[i] += (N // 10 + 1) * co

    nums[0] -= co
    co *= 10
    N //= 10

for num in nums:
    print(num, end=' ')