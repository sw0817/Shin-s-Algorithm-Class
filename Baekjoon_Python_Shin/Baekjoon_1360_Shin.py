# 백준 1360 되돌리기
# Baekjoon 1360

# Created by sw0817 on 2022. 09. 09..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1360

record = [[0, '']]
for i in range(int(input())):
    order = list(map(str, input().split()))
    if order[0] == 'type':
        record.append([int(order[2]), record[i][1] + order[1]])
    else:
        new_t = int(order[2]) - int(order[1])
        if new_t <= 0:
            record.append([int(order[2]), ''])
            continue
        elif record[i][0] < new_t:
            record.append([int(order[2]), record[i][1]])
            continue
        for j in range(i-1, -1, -1):
            if record[j][0] < new_t:
                record.append([int(order[2]), record[j][1]])
                break

print(record[-1][1])