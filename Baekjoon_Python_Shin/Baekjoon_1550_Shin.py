# 백준 1550 16진수
# Baekjoon 1550

# Created by sw0817 on 2021. 08. 28..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1550

num = input()
result = 0
for i in range(len(num)-1, -1, -1):
    try:
        result += (16 ** (len(num)-1-i)) * int(num[i])
    except:
        result += (16 ** (len(num)-1-i)) * (ord(num[i]) - 55)
print(result)