# 백준 5582 공통 부분 문자열
# Baekjoon 5582

# Created by sw0817 on 2021. 03. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5582

s1 = input()
s2 = input()
ls1 = len(s1)
ls2 = len(s2)

# dp[i][j] = s1[i], s2[j] 까지 연속된 공통 부분 문자열 길이
dp = [[0] * (ls2+1) for _ in range(ls1+1)]
for i in range(ls1):
    for j in range(ls2):

        # 직전 글자까지 공통 부분 문자열 길이 + 1
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1

# 최대 길이 출력
print(max(map(max, dp)))