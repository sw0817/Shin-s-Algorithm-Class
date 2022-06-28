# 백준 2420 사파리월드
# Baekjoon 2420

# Created by sw0817 on 2022. 06. 28..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2420

print(abs(sum((-1) ** idx * i for idx, i in enumerate(list(map(int, input().split()))))))