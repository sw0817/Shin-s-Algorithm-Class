# 백준 3865 학회원
# Baekjoon 3865

# Created by sw0817 on 2021. 12. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/3865

while True:
    n = int(input())
    if not n:
        break

    groups = dict()
    target = ''
    for _ in range(n):
        info = list(map(str, input().split(':')))
        if not target:
            target = info[0]
        groups[info[0]] = set(list(map(str, info[1][:-1].split(','))))

    for group in groups:
        for group2 in groups:
            if group != group2:
                if group in groups[group2]:
                    groups[group2] |= groups[group]

    result = len(groups[target])
    for group in groups:
        if group in groups[target]:
            result -= 1

    print(result)