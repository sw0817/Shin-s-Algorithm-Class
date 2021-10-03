# 백준 2583 영역 구하기
# Baekjoon 2583

# Created by sw0817 on 2020. 12. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2583

# 사방 탐색할 것
nexts = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 직사각형이 그려지지 않은 크기 구하기
def bfs(r, c):

    # 넓이 초기값
    num = 1

    # 빈 칸을 확인했음을 표시
    arr[r][c] = 1

    # 큐를 사용
    queue = [(r, c)]

    # 현재 위치에서 사방탐색하여 빈 칸이 있으면 넓이를 늘린다.
    while queue:
        r, c = queue.pop(0)
        for dr, dc in nexts:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < M and 0 <= nc < N and not arr[nr][nc]:
                queue.append((nr, nc))
                arr[nr][nc] = 1
                num += 1

    # 구해진 넓이를 결과 배열에 저장
    result.append(num)


# 세로 길이 M, 가로 길이 N, 직사각형 수 K
M, N, K = map(int, input().split())

# 모눈 종이 상태
arr = [[0] * N for _ in range(M)]

# 직사각형을 그린다.
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] += 1

# 결과값 배열
result = []

# 빈 칸이라면 주변 넓이 조사
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            bfs(i, j)

# 결과값 배열을 오름차순으로 정리
result.sort()

# 출력
print(len(result))
print(*result)