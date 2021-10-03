# 백준 2636 치즈
# Baekjoon 2636

# Created by sw0817 on 2021. 07. 04..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2636

from collections import deque

# 공기에 닿은 치즈 찾기
def check():
    # arr의 외곽은 치즈가 없어 모두 연결되어있다.
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * C for _ in range(R)]
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = 1
                # 치즈 만나면 녹을 치즈 배열에 추가
                if arr[nr][nc]:
                    melt_cheeze.append((nr, nc))
                    continue
                queue.append((nr, nc))


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(map(int, input().split())))

# 마지막 녹는 치즈 수
cnt = 0
# 시간
t = 0
while True:
    # while 문의 한 사이클은 1시간.
    # 이번 사이클에 녹는 치즈 배열
    melt_cheeze = deque()
    check()
    # 그 수
    temp = len(melt_cheeze)
    if temp:
        t += 1
        cnt = temp
        # 탐색이 끝나고 치즈를 녹인다.
        while melt_cheeze:
            r, c = melt_cheeze.popleft()
            arr[r][c] = 0
    # 녹을 치즈가 없다는건 다 녹았다는 의미.
    # 여기선 시간 늘릴 이유 없고 출력하면 끝.
    else:
        print(t)
        print(cnt)
        break


# def check(r, c):
#     check_queue = deque()
#     check_queue.append((r, c))
#     visited = [[0] * C for _ in range(R)]
#     visited[r][c] = 1
#     while check_queue:
#         check_r, check_c = check_queue.popleft()
#         for dr, dc in move:
#             nr, nc = check_r + dr, check_c + dc
#             if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] == 0:
#                 if nr == R-1 or nc == C-1 or nr == 0 or nc == 0:
#                     temp.append((r, c))
#                     return
#                 visited[nr][nc] = 1
#                 check_queue.append((nr, nc))
#
#
# move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# R, C = map(int, input().split())
# arr = []
# cheeze = []
#
# for i in range(R):
#     row = list(map(int, input().split()))
#     for j in range(C):
#         if row[j]:
#             cheeze.append((i, j))
#     arr.append(row)
#
# cnt = len(cheeze)
# t = 0
# temp = deque()
# while True:
#     for i, j in cheeze:
#         check(i, j)
#     t += 1
#     l = len(temp)
#     if cnt == l:
#         print(t)
#         print(cnt)
#         break
#     cnt -= l
#     while temp:
#         i, j = temp.popleft()
#         arr[i][j] = 0
#         cheeze.remove((i, j))