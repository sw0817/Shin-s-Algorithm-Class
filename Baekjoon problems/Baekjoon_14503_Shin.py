# 백준 14503 로봇 청소기
# Baekjoon 14503

# Created by sw0817 on 2021. 02. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14503

# next에서 1, 0 이 북쪽이라고 착각해서 오래걸렸네요..
next = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 시작 위치는 청소를 안 한 곳이므로 초기값은 1
result = 1

visited = [[0] * M for _ in range(N)]

# 시작 위치 청소로 시작
visited[r][c] = 1

# 청소가 불능일때까지
while True:
    clean = True

    # 사방 탐색을 하는데 왼쪽을 돌면서 한다.
    for i in range(4):
        d = (d+3) % 4
        dr, dc = next[d]
        nr = r + dr
        nc = c + dc

        # 왼쪽이 청소가 안 된 공간이면 청소하고 다시 while문 시작위치
        if not arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            result += 1
            r = nr
            c = nc
            clean = False
            break

    # 사방향 모두 청소하지 못했다면
    if clean:
        dr, dc = next[d]
        nr = r - dr
        nc = c - dc

        # 뒤가 뚫려있는지 확인해서 간다.
        if not arr[nr][nc]:
            r = nr
            c = nc
            continue

        # 뒤도 막혔으면 청소 종료
        else:
            break

print(result)