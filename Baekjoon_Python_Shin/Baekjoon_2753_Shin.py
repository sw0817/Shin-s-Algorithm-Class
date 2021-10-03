# 백준 2753 윤년
# Baekjoon 2753

# Created by sw0817 on 2021. 06. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2753

N = int(input())
if N % 400 == 0 or N % 4 == 0 and N % 100 != 0:
    print(1)
else:
    print(0)