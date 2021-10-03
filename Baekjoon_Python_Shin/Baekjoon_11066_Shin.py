# 백준 11066 파일 합치기
# Baekjoon 11066

# Created by sw0817 on 2021. 06. 29..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/11066

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    # i번째 장 까지의 누적합.

    sum_list = [0] * (N+1)
    for i in range(N):
        sum_list[i+1] = sum_list[i] + nums[i]

    # dp[i][j] == i ~ j 합치기 최소비용
    dp = [[0] * N for _ in range(N)]

    for btw in range(1, N):
        for start in range(N):
            end = start + btw
            if end == N:
                break
            dp[start][end] = 99999999999
            for i in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][i] + dp[i+1][end] + sum_list[end+1] - sum_list[start])

    print(dp[0][N-1])
