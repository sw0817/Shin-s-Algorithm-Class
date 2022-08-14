# 백준 10872 팩토리얼
# Baekjoon 10872

# Created by sw0817 on 2022. 08. 14..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10872

answer = 1
for i in range(int(input())):
    answer *= i + 1

print(answer)