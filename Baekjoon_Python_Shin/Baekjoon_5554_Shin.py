# 백준 5554 심부름 가는 길
# Baekjoon 5554

# Created by sw0817 on 2022. 10. 01..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/5554

t = 0
for _ in range(4):
    t += int(input())

print(t // 60)
print(t % 60)