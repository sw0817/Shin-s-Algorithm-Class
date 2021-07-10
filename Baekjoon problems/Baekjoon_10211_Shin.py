# 백준 10211 Maximum Subarray
# Baekjoon 10211

# Created by sw0817 on 2021. 07. 10..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10211

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    sub_sum = [0] * N
    sub_sum[0] = arr[0]
    for i in range(1, N):
        sub_sum[i] = sub_sum[i-1] + arr[i]
    result = sub_sum[0]
    for i in range(N):
        result = max(result, sub_sum[i])
        for j in range(i):
            result = max(result, sub_sum[i]-sub_sum[j])
    print(result)
