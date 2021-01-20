# 백준 1072 게임
# Baekjoon 1072

# Created by sw0817 on 2021. 01. 21..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1072

while True:
    try:
        x, y = map(int, input().split())
    except EOFError:
        break
    now_z = int(y*100/x)

    s, e = 1, 1000000000
    while s < e:
        m = (s+e)//2
        mv = int((y+m)*100/(x+m))
        if mv <= now_z:
            s = m+1
        else:
            e = m

    print(e if int((y+e)/(x+e)*100) > now_z else -1)