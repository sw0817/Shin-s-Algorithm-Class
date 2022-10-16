# 백준 1790 수 이어 쓰기 2
# Baekjoon 1790

# Created by sw0817 on 2022. 10. 16..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1790

N, k = map(int, input().split())
l, cnt = 1, 9

while l * cnt < k:
    k -= l * cnt
    l += 1
    cnt *= 10

k -= 1 # index 동치화
num = 10 ** (l-1) + k // l

if N < num:
    print(-1)
else:
    print(str(num)[k % l])