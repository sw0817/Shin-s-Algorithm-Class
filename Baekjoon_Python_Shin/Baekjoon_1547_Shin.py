# 백준 1547 공
# Baekjoon 1547

# Created by sw0817 on 2022. 09. 01..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1547

ans = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == ans:
        ans = b
    elif b == ans:
        ans = a

print(ans)