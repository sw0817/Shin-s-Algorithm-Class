# 백준 4179 불
# Baekjoon 4179

# Created by sw0817 on 2021. 07. 28..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/4179

from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

R, C = map(int, input().split())
arr = []
visited = [[[-1, -1] for _ in range(C)] for _ in range(R)]
suc = False
Jqueue = deque()
Fqueue = deque()

for i in range(R):
    row = list(input())
    for j in range(C):
        if row[j] == 'J':
            Jqueue.append((i, j))
            row[j] = '.'
            visited[i][j][0] = 0
            if i == 0 or i == R-1 or j == 0 or j == C-1:
                suc = True
        elif row[j] == 'F':
            Fqueue.append((i, j))
            row[j] = '.'
            visited[i][j][1] = 0
    arr.append(row)



cnt = 0
if suc:
    print(1)
while Jqueue and not suc:
    cnt += 1
    for _ in range(len(Fqueue)):
        Fr, Fc = Fqueue.popleft()
        for dr, dc in move:
            nFr, nFc = Fr + dr, Fc + dc
            if 0 <= nFr < R and 0 <= nFc < C and arr[nFr][nFc] == '.':
                if visited[Fr][Fc][1] + 1 < visited[nFr][nFc][1] or visited[nFr][nFc][1] == -1:
                    visited[nFr][nFc][1] = visited[Fr][Fc][1] + 1
                    Fqueue.append((nFr, nFc))

    for _ in range(len(Jqueue)):
        if suc:
            break
        Jr, Jc = Jqueue.popleft()
        for dr, dc in move:
            nJr, nJc = Jr + dr, Jc + dc
            if 0 <= nJr < R and 0 <= nJc < C and arr[nJr][nJc] == '.':
                if visited[Jr][Jc][0] + 1 < visited[nJr][nJc][0] or visited[nJr][nJc][0] == -1:
                    visited[nJr][nJc][0] = visited[Jr][Jc][0] + 1
                    if visited[nJr][nJc][0] < visited[nJr][nJc][1] or visited[nJr][nJc][1] == -1:
                        Jqueue.append((nJr, nJc))
                        if nJr == 0 or nJr == R-1 or nJc == 0 or nJc == C-1:
                            print(cnt + 1)
                            suc = True
                            break

if not suc:
    print('IMPOSSIBLE')

# for row in visited:
#     print(row)