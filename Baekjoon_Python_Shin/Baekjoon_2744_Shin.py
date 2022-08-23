# 백준 2744 대소문자 바꾸기
# Baekjoon 2744

# Created by sw0817 on 2022. 08. 23..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2744

result = ''
for a in input():
    if a != a.lower():
        result += a.lower()
    else:
        result += a.upper()

print(result)