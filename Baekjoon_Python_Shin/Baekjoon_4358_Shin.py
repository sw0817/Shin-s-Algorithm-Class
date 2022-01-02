# 백준 4358 생태학
# Baekjoon 4358

# Created by sw0817 on 2022. 01. 02..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4358

import sys

n = 0
trees = dict()
names = []
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    n += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
        names.append(tree)

names.sort()
for name in names:
    print('%s %.4f' % (name, round(trees[name] * 100 / n, 4)))