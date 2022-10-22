# 백준 1053 팰린드롬 공장
# Baekjoon 1053

# Created by sw0817 on 2022. 10. 22..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1053

def compDif(l, r):
    if word[l] == word[r]:
        return 0
    return 1


def solve(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if r <= l:
        return 0
    dp[l][r] = min(solve(l+1, r) + 1, solve(l, r-1) + 1, solve(l+1, r-1) + compDif(l, r))
    return dp[l][r]


word = list(input())
dp = [[-1] * 50 for _ in range(50)]
l = len(word)
result = solve(0, l - 1)
for i in range(l-1):
    for j in range(l):
        dp = [[-1] * 50 for _ in range(50)]
        word[i], word[j] = word[j], word[i]
        result = min(result, solve(0, l-1) + 1)
        word[i], word[j] = word[j], word[i]

print(result)