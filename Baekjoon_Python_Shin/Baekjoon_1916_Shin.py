# 백준 1916 최소비용 구하기
# Baekjoon 1916

# Created by sw0817 on 2021. 01. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1916

# 도시의 개수 N
N = int(input())

# 버스의 대수 M
M = int(input())

# 인접 리스트
adj = [[] for _ in range(N+1)]

# 출발지, 도착지, 비용
for _ in range(M):
    V1, V2, W = map(int, input().split())
    adj[V1].append([V2, W])

# 출발 도시, 도착 도시
start, end = map(int, input().split())

# 큰 수
INF = 100000 * 1000

# 비용 배열
visited = [INF] * (N+1)

# 시작점은 0의 비용
visited[start] = 0

# 현재 위치에서 기존보다 작은 비용으로 도착할 수 있는
# 정점의 비용을 초기화하며 큐에 추가한다.
queue = [start]
while queue:
    V = queue.pop(0)
    for V2, W in adj[V]:
        if visited[V] + W < visited[V2]:
            visited[V2] = visited[V] + W
            queue.append(V2)

# 최소비용 출력
print(visited[end])