# 백준 2754 학점계산
# Baekjoon 2754

# Created by sw0817 on 2022. 08. 21..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2754

hashMap = dict()
for i, alp in enumerate(['A', 'B', 'C', 'D', 'F']):
    hashMap[alp] = 4 - i

point = input()
if len(point) == 1:
    print(hashMap[point] + 0.0)
else:
    if point[1] == '0':
        print(hashMap[point[0]] + 0.0)
    elif point[1] == '+':
        print(hashMap[point[0]] + 0.3)
    else:
        print(hashMap[point[0]] - 0.3)