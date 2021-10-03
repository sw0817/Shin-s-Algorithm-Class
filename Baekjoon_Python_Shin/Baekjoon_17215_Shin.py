# 백준 17215 볼링 점수 계산
# Baekjoon 17215

# Created by sw0817 on 2020. 12. 07..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17215

def bow(idx):
    if info[idx] == 'S':
        num = 10
        if round < 10:
            plus.append(idx+1)
            plus.append(idx+2)
    elif info[idx] == 'P':
        num = 10 - temp
        if round < 10:
            plus.append(idx+1)
    elif info[idx] == '-':
        num = 0
    else:
        num = int(info[idx])
    return num


info = input()

score = 0
round = 1
chance = 2
plus = []

for i in range(len(info)):
    temp = bow(i)
    score += temp * (plus.count(i)+1)
    chance -= 1
    if info[i] == 'S' or chance == 0:
        chance = 2
        round += 1

print(score)