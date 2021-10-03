# 백준 1500 최대 곱
# Baekjoon 1500

# Created by sw0817 on 2021. 07. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1500

S, K = map(int, input().split())
rmn = S % K
print((S // K) ** (K-rmn) * (S // K + 1) ** rmn)