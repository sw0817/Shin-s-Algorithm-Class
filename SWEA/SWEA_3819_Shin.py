# SWEA 3819 [Professional] 최대 부분 배열
# SWEA 3819

# Created by sw0817 on 2021. 04. 13..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for tc in range(1, T+2):
    if tc != T + 1:
        N = int(input())
        arr = []
        for i in range(N):
            arr.append(int(input()))

        dp = [0] * N
        result = arr[0]
        dp[0] = result
        for i in range(1, N):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
            result = max(result, dp[i])

        print('#{} {}'.format(tc, result))