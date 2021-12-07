# 백준 2590 색종이
# Baekjoon 2590

# Created by sw0817 on 2021. 12. 07..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2590

paper = [0] * 6
for i in range(6):
    paper[i] = int(input())

result = 0
result += paper[5]
result += paper[4]
paper[0] -= min(paper[4] * 11, paper[0])
result += paper[3]
double = paper[1]
double_remain = paper[3] * 5
paper[1] -= min(double_remain, double)
double_remain -= min(double_remain, double)
one = paper[0]
paper[0] -= min(double_remain * 4, one)
triple = paper[2]
result += triple // 4
triple = triple % 4
if triple:
    result += 1
    triple = 4 - triple
    remain = triple * 9
    if paper[1]:
        double = paper[1]
        paper[1] -= min(double, triple * 2 - 1)
        remain -= min(double, triple * 2 - 1) * 4
    paper[0] -= min(paper[0], remain)
remain = paper[1] % 9
result += paper[1] // 9
if remain:
    result += 1
    paper[0] -= min(paper[0], 36 - remain * 4)
if paper[0]:
    result += paper[0] // 36
    paper[0] %= 36
if paper[0]:
    result += 1
print(result)
