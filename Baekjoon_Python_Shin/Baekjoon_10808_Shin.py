# 백준 10808 알파벳 개수
# Baekjoon 10808

# Created by sw0817 on 2022. 11. 11..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10808

alp = [0] * 26

for a in input():
    alp[ord(a)-97] += 1

print(*alp)