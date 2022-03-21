# 백준 1035 조각 움직이기
# Baekjoon 1035

# Created by sw0817 on 2022. 03. 21..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1035

import math
from collections import deque

def findMinDis(n, target):
    global minDisList
    queue = deque()
    queue.append(target+[0])
    minDisList[n][target[0]][target[1]] = 0
    while queue:
        r, c, cnt = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and cnt + 1 < minDisList[n][nr][nc]:
                minDisList[n][nr][nc] = cnt + 1
                queue.append([nr, nc, cnt + 1])


def findLinkedComb(k, n, l_idx, resultList):
    global linkedComb
    if k == n:
        if linkedCheck(resultList, n):
            linkedComb.append(resultList)
        return

    for i in range(5):
        if i < l_idx[0]:
            continue
        for j in range(5):
            if i == l_idx[0] and j <= l_idx[1]:
                continue
            nxtList = resultList[:]
            nxtList.append([i, j])
            findLinkedComb(k + 1, n, [i, j], nxtList)


def linkedCheck(arr, n):
    queue = []
    queue.append(arr[0])
    visited = [0] * n
    visited[0] = 1
    while queue:
        r, c = queue.pop()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and [nr, nc] in arr and visited[arr.index([nr, nc])] == 0:
                visited[arr.index([nr, nc])] = 1
                queue.append([nr, nc])
    if visited == [1] * n:
        return True
    return False


def findOrder(n, result):
    global order
    if len(result) == n:
        order.append(result)
        return

    for i in range(n):
        if i not in result:
            findOrder(n, result + [i])


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
inf = math.inf
answer = inf
targetList = []
linkedComb = []
order = []
for i in range(5):
    info = list(input())
    for j in range(5):
        if info[j] == '*':
            targetList.append([i, j])

minDisList = [[[inf] * 5 for _ in range(5)] for _ in range(len(targetList))]

for n in range(len(targetList)):
    findMinDis(n, targetList[n])

findLinkedComb(0, len(targetList), [-1, -1], [])
findOrder(len(targetList), [])

for comb in linkedComb:
    for nums in order:
        cur = 0
        for idx, num in enumerate(nums):
            r, c = comb[idx][0], comb[idx][1]
            cur += minDisList[num][r][c]
        answer = min(answer, cur)

print(answer)