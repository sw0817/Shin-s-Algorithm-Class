# 백준 10807 개수 세기
# Baekjoon 10807

# Created by sw0817 on 2022. 08. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10807

cnt = dict()
input()
for n in map(int, input().split()):
    if n in cnt:
        cnt[n] += 1
    else:
        cnt[n] = 1

n = int(input())
print(cnt[n] if n in cnt else 0)