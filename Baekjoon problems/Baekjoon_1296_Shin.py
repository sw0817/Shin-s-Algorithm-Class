# 백준 1296 데이트
# Baekjoon 1296

# Created by sw0817 on 2021. 09. 08..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1296

myName = input()
N = int(input())
names = []
myInfo = [0] * 4
max_num = 0
for alp in myName:
    if alp == 'L':
        myInfo[0] += 1
    elif alp == 'O':
        myInfo[1] += 1
    elif alp == 'V':
        myInfo[2] += 1
    elif alp == 'E':
        myInfo[3] += 1

for _ in range(N):
    L, O, V, E = myInfo
    girlName = input()
    for alp in girlName:
        if alp == 'L':
            L += 1
        elif alp == 'O':
            O += 1
        elif alp == 'V':
            V += 1
        elif alp == 'E':
            E += 1

    if max_num < ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100:
        max_num = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
        names = [girlName]
    elif max_num == ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100:
        names.append(girlName)

print(sorted(names)[0])