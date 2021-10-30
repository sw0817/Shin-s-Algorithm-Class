# 백준 1669 멍멍이 쓰다듬기
# Baekjoon 1669

# Created by sw0817 on 2021. 10. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1669

X, Y = map(int, input().split())

if Y - X == 0:
    print(0)
else:
    bet = int((Y - X) ** 0.5)
    if bet ** 2 == Y - X:
        print(bet * 2 - 1)
    else:
        rem = Y - X - bet ** 2
        if rem <= bet:
            print(bet * 2)
        else:
            print(bet * 2 + 1)