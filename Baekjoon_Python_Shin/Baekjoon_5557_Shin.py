# 백준 5557 1학년
# Baekjoon 5557

# Created by sw0817 on 2021. 08. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5557

N = int(input())
nums = list(map(int, input().split()))
right = nums[-1]
dp = [[0] * 21 for _ in range(N-1)]
dp[0][nums[0]] = 1
for i in range(1, N-1):
    num = nums[i]
    for j in range(21):
        if dp[i-1][j]:
            if 0 <= num + j <= 20:
                dp[i][num+j] += dp[i-1][j]
            if 0 <= j - num <= 20:
                dp[i][j-num] += dp[i-1][j]

print(dp[N-2][right])