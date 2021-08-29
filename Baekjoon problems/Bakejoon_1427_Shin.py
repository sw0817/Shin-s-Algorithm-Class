# 백준 1427 소트인사이드
# Baekjoon 1427

# Created by sw0817 on 2021. 08. 29..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1427

num = input()
num = sorted(num, reverse=True)
print("".join(num))