# 백준 1230 문자열 거리
# Baekjoon 1230

# Created by sw0817 on 2021. 04. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1230

def main():
    str1 = input()
    str2 = input()
    l1 = len(str1)
    l2 = len(str2)

    if l2 < l1:
        return -1

    dp = [[[-1] * 2 for _ in range(l2+1)] for _ in range(l2+1)]
    dp[0][0][0] = 0
    dp[0][0][1] = 1000
    for i in range(1, l2):
        dp[0][i][0] = 1000
        dp[0][i][1] = 1

    for i in range(l1):
        for j in range(i+1):
            dp[i+1][j][0] = dp[i+1][j][1] = 1000
        for j in range(i, l2):
            if str1[i] == str2[j]:
                dp[i+1][j+1][0] = min(dp[i][j][0], dp[i][j][1])
            else:
                dp[i+1][j+1][0] = 1000
            dp[i+1][j+1][1] = min(dp[i+1][j][0]+1, dp[i+1][j][1])

    result = min(dp[l1][l2][0], dp[l1][l2][1])
    if 1000 <= result:
        result = -1

    print(result)

main()