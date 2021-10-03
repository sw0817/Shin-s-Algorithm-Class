# 백준 2884 알람 시계
# Baekjoon 2884

# Created by sw0817 on 2021. 06. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())
if 45 <= M:
    M -= 45
else:
    M += 15
    H -= 1
if H < 0:
    H = 23
print(H, M)