# 백준 14238 출근 기록
# Baekjoon 14238

# Created by sw0817 on 2021. 08. 10..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14238

def cal(a, b, c, pre, dPre, word):
    if finish:
        return

    if a == aCnt and b == bCnt and c == cCnt:
        print(word)
        finish.append(True)
        return True

    if dp[a][b][c][pre][dPre]:
        return

    dp[a][b][c][pre][dPre] = True

    if a < aCnt:
        cal(a+1, b, c, 0, pre, word + 'A')

    if b < bCnt and pre != 1:
        cal(a, b+1, c, 1, pre, word + 'B')

    if c < cCnt and pre != 2 and dPre != 2:
        cal(a, b, c+1, 2, pre, word + 'C')


S = input()
L = len(S)
aCnt = S.count('A')
bCnt = S.count('B')
cCnt = S.count('C')

dp = [[[[[0] * 3 for _ in range(3)] for _ in range(50)] for _ in range(50)] for _ in range(50)]
finish = []
cal(0, 0, 0, 0, 0, '')
if not finish:
    print(-1)