# 백준 1234 크리스마스 트리
# Baekjoon 1234

# Created by sw0817 on 2022. 01. 06..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1234

def makeTree(deep, r, g, b):
    if dp[deep][r][g][b] != -1:
        return dp[deep][r][g][b]

    dp[deep][r][g][b] = 0
    if deep == N:
        dp[deep][r][g][b] = 1
        return 1

    # 단색으로 채우기
    if r + deep + 1 <= R:
        dp[deep][r][g][b] += makeTree(deep+1, r+deep+1, g, b)
    if g + deep + 1 <= G:
        dp[deep][r][g][b] += makeTree(deep+1, r, g+deep+1, b)
    if b + deep + 1 <= B:
        dp[deep][r][g][b] += makeTree(deep+1, r, g, b+deep+1)

    # 깊이가 짝수면 두 가지 색으로 채워야 함
    if not (deep + 1) % 2:
        cnt = (deep + 1) // 2
        if r + cnt <= R and g + cnt <= G:
            dp[deep][r][g][b] += makeTree(deep+1, r+cnt, g+cnt, b) * (factorial[deep+1] // (factorial[cnt] ** 2))
        if r + cnt <= R and b + cnt <= B:
            dp[deep][r][g][b] += makeTree(deep+1, r+cnt, g, b+cnt) * (factorial[deep+1] // (factorial[cnt] ** 2))
        if g + cnt <= G and b + cnt <= B:
            dp[deep][r][g][b] += makeTree(deep+1, r, g+cnt, b+cnt) * (factorial[deep+1] // (factorial[cnt] ** 2))

    # 깊이가 3의 배수면 세 가지 색으로
    if not (deep + 1) % 3:
        cnt = (deep + 1) // 3
        if r + cnt <= R and g + cnt <= G and b + cnt <= B:
            dp[deep][r][g][b] += makeTree(deep+1, r+cnt, g+cnt, b+cnt) * (factorial[deep+1] // (factorial[cnt] ** 3))

    return dp[deep][r][g][b]


factorial = [1] + [0] * 100
for i in range(1, 101):
    factorial[i] = factorial[i-1] * i

N, R, G, B = map(int, input().split())
result = 0
# dp[d][r][g][b] : 깊이 d에서 색 r,g,b 개 사용해서 만들 수 있는 트리 수
dp = [[[[-1] * 101 for _ in range(101)] for _ in range(101)] for _ in range(11)]
if R:
    makeTree(1, 1, 0, 0)
if G:
    makeTree(1, 0, 1, 0)
if B:
    makeTree(1, 0, 0, 1)

if dp[1][1][0][0] != -1:
    result += dp[1][1][0][0]
if dp[1][0][1][0] != -1:
    result += dp[1][0][1][0]
if dp[1][0][0][1] != -1:
    result += dp[1][0][0][1]

print(result)