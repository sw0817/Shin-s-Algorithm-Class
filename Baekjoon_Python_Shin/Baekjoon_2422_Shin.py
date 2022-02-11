# 백준 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# Baekjoon 2422

# Created by sw0817 on 2022. 02. 11..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2422

N, M = map(int, input().split())
adj = [[False for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = True
    adj[b][a] = True

result = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            if not adj[i][j] and not adj[i][k] and not adj[j][k]:
                result += 1

print(result)