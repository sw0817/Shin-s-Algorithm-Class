# 백준 1167 트리의 지름
# Baekjoon 1167

# Created by sw0817 on 2021. 02. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1167

def dfs(v, w):
    global weight, target_v
    for next_v, next_w in adj[v]:
        if visited[next_v]:
            continue
        visited[next_v] = 1
        if weight < w + next_w:
            weight = w + next_w
            target_v = next_v
        dfs(next_v, w+next_w)
        visited[next_v] = 0


V = int(input())

# 트리 정보
adj = [[] for _ in range(V+1)]

for i in range(V):
    # 트리 정보 받기
    info = list(map(int, input().split()))
    s = info[0]
    j = 1
    while info[j] != -1:
        adj[s].append((info[j], info[j+1]))
        j += 2

# 트리는 어느 정점이든 모든 정점으로 갈 수 있고 막다른 정점이 있음
# 아무데서나 가장 먼 막다른 정점에서부터, 다시 가장 먼 막다른 정점의 길이가
# 트리의 최대 길이(지름)

# 이동 길이
weight = 0

# 첫 막다른 정점이 될 녀석
target_v = -1

# 방문 배열
visited = [0] * (V+1)

# 1번 정점에서 출발
visited[1] = 1
dfs(1, 0)

# 1번 정점으로부터 가장 먼 막다른 정점
start = target_v

# 이동길이랑 막다른 정점 될 놈, 방문배열 초기화
weight = 0
target_v = -1
visited = [0] * (V+1)

# start에서 다시 시작
visited[start] = 1
dfs(start, 0)

# 최대 길이 출력
print(weight)