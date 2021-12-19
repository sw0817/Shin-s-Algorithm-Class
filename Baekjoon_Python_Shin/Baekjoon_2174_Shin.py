# 백준 2174 로봇 시뮬레이션
# Baekjoon 2174

# Created by sw0817 on 2021. 12. 20..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2174

A, B = map(int, input().split())
N, M = map(int, input().split())
location = []
visited = [[0] * A for _ in range(B)]
# 북서남동
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for i in range(N):
    c, r, d = map(str, input().split())
    if d == 'N':
        d = 0
    elif d == 'W':
        d = 1
    elif d == 'S':
        d = 2
    else:
        d = 3
    location.append([B-int(r), int(c)-1, d])
    visited[B-int(r)][int(c)-1] = i+1

result = 'OK'
done = False
for _ in range(M):
    n, s, c = map(str, input().split())
    if done:
        continue
    n, c = int(n)-1, int(c)
    if s == 'L':
        location[n][2] = (location[n][2] + c) % 4
    elif s == 'R':
        location[n][2] = (location[n][2] - c) % 4
    else:
        cr, cc = location[n][0], location[n][1]
        visited[cr][cc] = 0
        dr, dc = dir[location[n][2]]
        for _ in range(c):
            if done:
                break
            cr += dr
            cc += dc
            if 0 <= cr < B and 0 <= cc < A:
                if visited[cr][cc]:
                    result = 'Robot {} crashes into robot {}'.format(n+1, visited[cr][cc])
                    done = True
                    break
            else:
                result = 'Robot {} crashes into the wall'.format(n+1)
                done = True
                break
        if done:
            continue
        visited[cr][cc] = n+1
        location[n][0], location[n][1] = cr, cc

print(result)