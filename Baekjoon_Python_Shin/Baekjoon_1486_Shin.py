# 백준 1486 등산
# Baekjoon 1486

# Created by sw0817 on 2021. 11. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1486

import heapq

def down(i, j):
    global result
    if arr[i][j] <= result:
        return
    cur = distance[i][j]
    down_dist = [[INF] * M for _ in range(N)]
    down_queue = []
    heapq.heappush(down_queue, (cur, [i, j]))
    down_dist[i][j] = cur
    while down_queue:
        dist, now = heapq.heappop(down_queue)
        if D < dist:
            return
        else:
            if now == [0, 0]:
                result = max(result, arr[i][j])
                return
        r, c = now
        if down_dist[r][c] < dist:
            continue
        for info in adj[r][c]:
            cost = dist + info[1]
            nr, nc = info[0]
            if cost < down_dist[nr][nc]:
                down_dist[nr][nc] = cost
                heapq.heappush(down_queue, (cost, [nr, nc]))


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M, T, D = map(int, input().split())
result = 0
arr = [[0] * M for _ in range(N)]
for i in range(N):
    info = input()
    for j in range(M):
        h = info[j]
        if ord(h) <= 90:
            arr[i][j] = ord(h) - 65
        else:
            arr[i][j] = ord(h) - 71

# 시작은 0, 0
# 시작점에서 모든 점에 대한 다익스트라를 구한다.
INF = int(1e9)
adj = [[[] for _ in range(M)] for _ in range(N)]
# 모든 정점에서 갈 수 있는 정점으로의 거리 배열 만들건데,
# 효율을 위해 격자식으로 탐색할 것

for i in range(0, N, 2):
    for j in range(0, M, 2):
        cur_h = arr[i][j]
        for dr, dc in move:
            nr, nc = i + dr, j + dc
            if 0 <= nr < N and 0 <= nc < M:
                h = arr[nr][nc]
                if T < abs(cur_h - h):
                    continue
                if cur_h < h:
                    adj[i][j].append([[nr, nc], abs(h-cur_h) ** 2])
                    adj[nr][nc].append([[i, j], 1])
                elif h < cur_h:
                    adj[nr][nc].append([[i, j], abs(h - cur_h) ** 2])
                    adj[i][j].append([[nr, nc], 1])
                else:
                    adj[nr][nc].append([[i, j], 1])
                    adj[i][j].append([[nr, nc], 1])

for i in range(1, N, 2):
    for j in range(1, M, 2):
        cur_h = arr[i][j]
        for dr, dc in move:
            nr, nc = i + dr, j + dc
            if 0 <= nr < N and 0 <= nc < M:
                h = arr[nr][nc]
                if T < abs(cur_h - h):
                    continue
                if cur_h < h:
                    adj[i][j].append([[nr, nc], abs(h - cur_h) ** 2])
                    adj[nr][nc].append([[i, j], 1])
                elif h < cur_h:
                    adj[nr][nc].append([[i, j], abs(h - cur_h) ** 2])
                    adj[i][j].append([[nr, nc], 1])
                else:
                    adj[nr][nc].append([[i, j], 1])
                    adj[i][j].append([[nr, nc], 1])

# 다익스트라로 올라가는 시간 구함
distance = [[INF] * M for _ in range(N)]
queue = []
heapq.heappush(queue, (0, [0, 0]))
distance[0][0] = 0
while queue:
    dist, now = heapq.heappop(queue)
    r, c = now
    if distance[r][c] < dist:
        continue
    for i in adj[r][c]:
        cost = dist + i[1]
        nr, nc = i[0]
        if cost < distance[nr][nc]:
            distance[nr][nc] = cost
            heapq.heappush(queue, (cost, [nr, nc]))

    # 모든 점에 대해 내려가는 시간 구하기
    # 불가능하면 스킵
    for i in range(N):
        for j in range(M):
            down(i, j)

print(result)