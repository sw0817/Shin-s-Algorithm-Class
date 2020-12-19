# 백준 1085 직사각형에서 탈출
# Baekjoon 1085

# Created by sw0817 on 2020. 12. 19..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

print(min([x, y, w-x, h-y]))