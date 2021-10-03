# 백준 1181 단어 정렬
# Baekjoon 1181

# Created by sw0817 on 2021. 08. 17..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1181

N = int(input())
lst = []
for _ in range(N):
    lst.append(input())
lst = list(set(lst))
lst.sort(key=lambda x:[len(x), x])
for word in lst:
    print(word)