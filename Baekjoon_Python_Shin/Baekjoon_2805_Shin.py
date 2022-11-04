# 백준 2805 나무 자르기
# Baekjoon 2805

# Created by sw0817 on 2022. 11. 04..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

l = 1
r = trees[-1]
result = 0

while l <= r:
    H = 0
    mid = (l + r) // 2

    for t in trees:
        if mid < t:
            H += t - mid

    if H < M:
        r = mid - 1

    else:
        result = mid
        l = mid + 1

print(result)