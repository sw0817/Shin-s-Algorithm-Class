# 백준 1940 주몽
# Baekjoon 1940

# Created by sw0817 on 2022. 10. 04..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1940

N = int(input())
M = int(input())

nums = list(map(int, input().split()))
nums.sort()

s, e = 0, len(nums) - 1
cnt = 0

while s < e:
    cur = nums[s] + nums[e]
    if cur == M:
        cnt += 1
        s += 1
        e -= 1
    elif cur < M:
        s += 1
    else:
        e -= 1

print(cnt)
