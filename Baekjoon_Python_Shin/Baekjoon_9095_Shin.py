# 백준 9095 1, 2, 3 더하기
# Baekjoon 9095

# Created by sw0817 on 2021. 12. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9095

dp = [0, 1, 2, 4] + [0] * 8
nxt = 3
for i in range(4, 12):
    nxt += dp[i-1] - dp[i-4]
    dp[i] = nxt

for _ in range(int(input())):
    print(dp[int(input())])