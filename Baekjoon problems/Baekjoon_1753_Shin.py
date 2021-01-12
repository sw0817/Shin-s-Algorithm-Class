# 백준 1753 최단경로
# Baekjoon 1753

# Created by sw0817 on 2021. 01. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1753

# 우선순위 큐를 사용한다. (다익스트라)
import heapq


# 정점의 개수 V, 간선의 개수 E
V, E = map(int, input().split())

# 시작 정점 K
K = int(input())

# 인접 리스트
adj = [[] for _ in range(V+1)]

# 시작 정점 u, 도착 정점 v, 가중치 w (방향 그래프)
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

# 큰 수
INF = 20000 * 10 + 1

# 최소비용 배열
visited = [INF] * (V+1)

# 시작 비용은 0
visited[K] = 0

# 시작점부터 시작해 기존 비용보다 작은 비용으로 움직일 수 있는
# 간선의 비용 초기화 및 큐 추가 반복
queue = []
heapq.heappush(queue, [0, K])

while queue:
    temp, u = heapq.heappop(queue)
    for v, w in adj[u]:
        if temp + w < visited[v]:
            visited[v] = temp + w
            heapq.heappush(queue, [temp+w, v])

# 조건에 맞게 출력
for i in range(1, V+1):
    if visited[i] == INF:
        print('INF')
    else:
        print(visited[i])