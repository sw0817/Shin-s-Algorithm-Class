# 백준 10251 운전 면허 시험
# Baekjoon 10251

# Created by sw0817 on 2021. 03. 15..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10251

n = int(input())
word = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]
al = [0] * 26

for i in range(n):
    num = 0
    for j in word[i][::-1]:
        al[j] += (10 ** num)
        num += 1

al.sort(reverse=True)

ans = 0
num = 9
idx = 0

while al[idx] and idx < 26:
    ans += al[idx] * num
    idx += 1
    num -= 1

print(ans)
