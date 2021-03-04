# 백준 2758 로또
# Baekjoon 2758

# Created by sw0817 on 2021. 03. 01..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2758

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    # m까지의 숫자로 n개 로또 번호 만드는 방법 수
    dp = [[0] * (m+1) for _ in range(n)]

    # 0은 없고, 1개 로또 번호 만드는 방법은 m개이다.
    for i in range(m+1):
        dp[0][i] = i

    # 2개 이상의 로또 번호를 만드는 경우
    for i in range(1, n):

        # 다음 수는 이전 수의 2배 이상이어야 하므로, m < 2^i 는 불가능
        for j in range(2 ** i, m+1):

            # dp[i][j]는 m == j-1 일때 만들 수 있는 수 + 새로운 m 활용하는 수
            # 새로운 m은 i가 1작고 j가 m // 2 인 경우에 가능
            dp[i][j] = dp[i-1][j//2] + dp[i][j-1]

    # 해당 조건 dp 출력력
    print(dp[n-1][m])