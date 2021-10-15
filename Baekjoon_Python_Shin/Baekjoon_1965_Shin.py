# 백준 1965 상자넣기
# Baekjoon 1965

# Created by sw0817 on 2021. 10. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1965

N = int(input())
boxes = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if boxes[j] < boxes[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))