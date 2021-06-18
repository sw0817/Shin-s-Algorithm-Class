# 백준 1248 맞춰봐
# Baekjoon 1248

# Created by sw0817 on 2021. 06. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1248

def check(idx):
    sum_ = 0
    for i in range(idx, -1, -1):
        sum_ += result[i]
        if sum_ == 0 and S[i][idx] != 0:
            return False
        elif sum_ < 0 and S[i][idx] >= 0:
            return False
        elif sum_ > 0 and S[i][idx] <= 0:
            return False
    return True

def solve(idx):
    if idx == N:
        return True
    if S[idx][idx] == 0:
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        result[idx] = S[idx][idx] * i
        if check(idx) and solve(idx+1):
            return True
    return False


N = int(input())
sign = list(input())
S = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        temp = sign.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

result = [0] * N
solve(0)
print(' '.join(map(str, result)))