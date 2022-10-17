# 백준 5721 사탕 줍기 대회
# Baekjoon 5721

# Created by sw0817 on 2022. 10. 17..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5721

while True:
    # 입력부
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(n)]

    # dp : 열을 기준으로 한 다이나믹 프로그래밍 배열
    # dp[i][j][0] = i행 까지 j열을 뽑지 않을 때 사탕의 최대값
    # dp[i][j][1] = i행 까지 j열을 뽑을 때 사탕의 최대값
    dp = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0][1] = arr[i][0]

    # 점화식
    for i in range(n):
        for j in range(1, m):
            dp[i][j][1] = dp[i][j - 1][0] + arr[i][j]
            dp[i][j][0] = max(dp[i][j - 1][0], dp[i][j - 1][1])

    # val : 현재 i번째 행에서 얻을 수 있는 사탕의 최대값
    val = [0] * n
    for i in range(n):
        temp = 0
        for j in range(m):
            temp = max(temp, dp[i][j][0], dp[i][j][1])
        val[i] = temp

    # dp2 : 행을 기준으로 한 다이나믹 프로그래밍 배열
    # dp2[i][0] = 현재 i번째 행을 뽑지 않을 때 얻는 사탕의 최대값
    # dp2[i][1] = 현재 i번째 행을 뽑을 때 얻는 사탕의 최대값
    dp2 = [[0] * 2 for _ in range(n)]
    dp2[0][1] = val[0]

    # 점화식
    for i in range(1, n):
        dp2[i][1] = dp2[i - 1][0] + val[i]
        dp2[i][0] = max(dp2[i - 1][0], dp2[i - 1][1])

    # 정답 출력
    print(max(dp2[n - 1][0], dp2[n - 1][1]))