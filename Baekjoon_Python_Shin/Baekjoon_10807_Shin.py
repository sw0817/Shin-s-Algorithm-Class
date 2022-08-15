# 백준 10807 개수 세기
# Baekjoon 10807

# Created by sw0817 on 2022. 08. 15..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10807

cnt = [0] * 101
input()
for n in map(int, input().split()):
    cnt[n] += 1

print(cnt[int(input())])