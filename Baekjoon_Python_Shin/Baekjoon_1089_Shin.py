# 백준 1089 스타트링크 타워
# Baekjoon 1089

# Created by sw0817 on 2022. 01. 19..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1089

N = int(input())
info = [list(input()) for _ in range(5)]
nums = [set(i for i in range(10)) for _ in range(N)]
result = 0
for k in range(N):
    if result == -1:
        break
    if info[0][k*3+k] == '#':
        nums[k].discard(1)
    if info[0][k*3+k+1] == '#':
        nums[k].discard(4)
        nums[k].discard(1)
    if info[1][k*3+k] == '#':
        nums[k].discard(1)
        nums[k].discard(2)
        nums[k].discard(3)
        nums[k].discard(7)
    if info[1][k*3+k+1] == '#':
        result = -1
        break
    if info[1][k*3+k+2] == '#':
        nums[k].discard(5)
        nums[k].discard(6)
    if info[2][k*3+k] == '#':
        nums[k].discard(1)
        nums[k].discard(7)
    if info[2][k*3+k+1] == '#':
        nums[k].discard(0)
        nums[k].discard(1)
        nums[k].discard(7)
    if info[3][k*3+k] == '#':
        nums[k].discard(1)
        nums[k].discard(3)
        nums[k].discard(4)
        nums[k].discard(5)
        nums[k].discard(7)
        nums[k].discard(9)
    if info[3][k*3+k+1] == '#':
        result = -1
        break
    if info[3][k*3+k+2] == '#':
        nums[k].discard(2)
    if info[4][k*3+k] == '#':
        nums[k].discard(1)
        nums[k].discard(4)
        nums[k].discard(7)
    if info[4][k*3+k+1] == '#':
        nums[k].discard(1)
        nums[k].discard(4)
        nums[k].discard(7)

if result == -1:
    print(-1)
else:
    result = 0
    cnt = 1
    for i in range(N):
        cnt *= len(nums[i])

    for i in range(N):
        n = sum(nums[i]) * (10 ** (N-1-i))
        c = cnt // len(nums[i])
        result += n * c

    print(result / cnt)