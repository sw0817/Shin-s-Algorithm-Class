# 백준 11053 가장 긴 증가하는 부분 수열
# Baekjoon 11053

# Created by sw0817 on 2021. 08. 11..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11053

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))