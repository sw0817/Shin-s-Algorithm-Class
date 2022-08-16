# 백준 5597 과제 안 내신 분..?
# Baekjoon 5597

# Created by sw0817 on 2022. 08. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5597

submit = [1] + [0] * 30
for _ in range(28):
    submit[int(input())] = 1

for i in range(1, 31):
    if not submit[i]:
        print(i)