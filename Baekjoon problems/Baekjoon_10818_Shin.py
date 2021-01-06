# 백준 10818 최소, 최대
# Baekjoon 10818

# Created by sw0817 on 2020. 01. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10818

N = int(input())

numbers = list(map(int, input().split()))
print('{} {}'.format(min(numbers), max(numbers)))