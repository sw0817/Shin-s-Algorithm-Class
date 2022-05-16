# 백준 2138 전구와 스위치
# Baekjoon 2138

# Created by sw0817 on 2022. 05. 16..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2138

N = int(input())
nums = ['1', '0']
cur1 = list(input())
ret = input()
cur2 = cur1[:]
cnt1 = 0
cnt2 = 1
for i in range(2):
    cur2[i] = nums[int(cur2[i])]

result = -1
for i in range(1, N-1):
    if cur1[i-1] != ret[i-1]:
        cnt1 += 1
        cur1[i] = nums[int(cur1[i])]
        cur1[i+1] = nums[int(cur1[i+1])]

    if cur2[i-1] != ret[i-1]:
        cnt2 += 1
        cur2[i] = nums[int(cur2[i])]
        cur2[i+1] = nums[int(cur2[i+1])]

if cur1[N-2] != ret[N-2]:
    cnt1 += 1
    cur1[N-2] = nums[int(cur1[N-2])]
    cur1[N-1] = nums[int(cur1[N-1])]

if cur2[N-2] != ret[N-2]:
    cnt2 += 1
    cur2[N-2] = nums[int(cur2[N-2])]
    cur2[N-1] = nums[int(cur2[N-1])]

if cur2[N-1] == ret[N-1]:
    result = cnt2

if cur1[N-1] == ret[N-1]:
    result = cnt1

print(result)