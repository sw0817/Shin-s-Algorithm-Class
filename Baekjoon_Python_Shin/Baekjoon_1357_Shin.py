# 백준 1357 뒤집힌 덧셈
# Baekjoon 1357

# Created by sw0817 on 2021. 12. 18..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1357

def change(s):
    n = ''
    idx = len(s) - 1
    while 0 <= idx and s[idx] == '0':
        idx -= 1

    while 0 <= idx:
        n += s[idx]
        idx -= 1

    return int(n)


X, Y = map(str, input().split())
print(change(str(change(X) + change(Y))))