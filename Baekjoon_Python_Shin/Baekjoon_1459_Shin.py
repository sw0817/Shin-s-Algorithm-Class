# 백준 1459 걷기
# Baekjoon 1459

# Created by sw0817 on 2022. 11. 14..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1459

X, Y, W, S = map(int, input().split())
if W * 2 <= S:
    print((X + Y) * W)
else:
    result, remain = min(X, Y) * S, abs(X - Y)
    if S < W:
        print(result + (remain - 1) * S + W if remain % 2 else result + remain * S)
    else:
        print(result + remain * W)