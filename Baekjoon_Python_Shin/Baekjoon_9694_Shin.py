# 백준 9694 무엇을 아느냐가 아니라 누구를 아느냐가 문제다
# Baekjoon 9694

# Created by sw0817 on 2020. 12. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9694

# 전형적인 다익스트라 문제
T = int(input())

for tc in range(1, T+1):

    # 관계의 수 N, 정치인의 수 M
    N, M = map(int, input().split())

    # x가 가진 y와의 친밀도 배열
    adj = [[] for _ in range(M)]

    for i in range(N):

        # 정치인 1, 2, 친밀도
        x, y, z = map(int, input().split())
        adj[x].append((y, z))
        adj[y].append((x, z))

    # 무한대
    INF = 999999

    # 선택 배열
    selected = [False] * M

    # 0번 즉 한신이로부터 친밀도 배열
    dist = [[INF]] * M

    # 자기 자신과의 친밀도는 0
    dist[0] = [0]
    cnt = 0

    # 다익스트라
    while cnt <= N-1:
        minV = INF
        minIdx = -1
        for i in range(M):
            if not selected[i] and dist[i][0] < minV:
                minV = dist[i][0]
                minIdx = i

        selected[minIdx] = True
        cnt += 1
        for w, cost in adj[minIdx]:
            if dist[w][0] > minV + cost:

                # 역추적을 위해 누구로부터 연결되었는지 표시
                dist[w] = [minV + cost, minIdx]

    # 친밀도 형성이 불가능하다면
    if len(adj[M-1]) == 1:
        print('Case #{}: -1'.format(tc))

    else:
        print('Case #{}:'.format(tc), end=' ')
        result = '{}'.format(M-1)

        # 역추적
        idx = M-1
        while idx != 0:
            idx = dist[idx][1]
            result = str(idx) + ' ' + result

        print(result)