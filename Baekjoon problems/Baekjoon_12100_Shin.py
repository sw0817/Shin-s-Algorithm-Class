# 백준 12100 2048 (Easy)
# Baekjoon 12100

# Created by sw0817 on 2021. 04. 10..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/12100

from copy import deepcopy
from _collections import deque

def recursive(d, arr, cnt):
    global result
    array = deepcopy(arr)

    if d == 0:
        for i in range(N):
            temp = deque()
            for j in range(N):
                if array[j][i] != 0:
                    temp.append(array[j][i])

            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num + 1]:
                    temp[num] = 0
                    temp[num+1] *= 2
                    num += 2
                else:
                    num += 1

            num = 0
            while num < N:
                if temp:
                    cur = temp.popleft()
                    if cur != 0:
                        array[num][i] = cur
                        num += 1
                else:
                    array[num][i] = 0
                    num += 1

    elif d == 1:
        for i in range(N):
            temp = deque()
            for j in range(N-1, -1, -1):
                if array[j][i] != 0:
                    temp.append(array[j][i])

            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num+1]:
                    temp[num] = 0
                    temp[num+1] *= 2
                    num += 2
                else:
                    num += 1

            num = N - 1
            while -1 < num:
                if temp:
                    cur = temp.popleft()
                    if cur != 0:
                        array[num][i] = cur
                        num -= 1
                else:
                    array[num][i] = 0
                    num -= 1

    elif d == 2:
        for i in range(N):
            temp = deque()
            for j in range(N-1, -1, -1):
                if array[i][j] != 0:
                    temp.append(array[i][j])

            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num + 1]:
                    temp[num] = 0
                    temp[num + 1] *= 2
                    num += 2
                else:
                    num += 1

            num = N - 1
            while -1 < num:
                if temp:
                    cur = temp.popleft()
                    if cur != 0:
                        array[i][num] = cur
                        num -= 1
                else:
                    array[i][num] = 0
                    num -= 1

    elif d == 3:
        for i in range(N):
            temp = deque()
            for j in range(N):
                if array[i][j] != 0:
                    temp.append(array[i][j])

            num = 0
            while num + 1 < len(temp):
                if temp[num] == temp[num + 1]:
                    temp[num] = 0
                    temp[num + 1] *= 2
                    num += 2
                else:
                    num += 1

            num = 0
            while num < N:
                if temp:
                    cur = temp.popleft()
                    if cur != 0:
                        array[i][num] = cur
                        num+= 1
                else:
                    array[i][num] = 0
                    num += 1

    if cnt == 5:
        for i in range(N):
            result = max(result, max(array[i]))
        return

    recursive(0, array, cnt + 1)
    recursive(1, array, cnt + 1)
    recursive(2, array, cnt + 1)
    recursive(3, array, cnt + 1)


N = int(input())
result = 0
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(4):
    recursive(i, arr, 1)

print(result)