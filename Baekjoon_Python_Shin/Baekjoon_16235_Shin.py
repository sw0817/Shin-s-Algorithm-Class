# 백준 16235 나무 재테크
# Baekjoon 16235

# Created by sw0817 on 2021. 04. 16..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/16235

# 빠른 실행속도를 위한 deque
from _collections import deque

# 가을 번식 방향
around = [(1, 0), (1, 1), (0, 1), (-1, -1), (-1 ,0), (0, -1), (1, -1), (-1, 1)]

# 땅 크기 N, 나무 정보 M, 재테크 기간 K년
N, M, K = map(int, input().split())

# 겨울 양분 배열
A = [list(map(int, input().split())) for _ in range(N)]

# 나무 배열
arr = [[deque() for _ in range(N)] for _ in range(N)]

# 나무를 심는다. 어린 나무부터 배열의 왼쪽에 오게 할 것이고,
# 처음에는 한 위치에 나무 한 그루만 있으므로 그냥 append
for _ in range(M):
    r, c, age = map(int, input().split())
    arr[r-1][c-1].append(age)

# 양분 배열
nut = [[5] * N for _ in range(N)]

# 가을에 자라날 자식 나무 수 배열
child = [[0] * N for _ in range(N)]

# K년간 시뮬레이션
for i in range(K):
    # 봄
    for r in range(N):
        for c in range(N):
            # 봄이 지난 뒤 남는 나무
            temp = deque()
            # 죽은 나무 양분 양
            die = 0
            # 모든 나무에 대해
            while arr[r][c]:
                tree = arr[r][c].popleft()
                # 양분이 충분하면
                if tree <= nut[r][c]:
                    # 커서 나이가 5의 배수면
                    if tree % 5 == 4:
                        # 자식 수 + 1
                        child[r][c] += 1
                    # 양분 먹기
                    nut[r][c] -= tree
                    # 나이 먹어서 배열에 담기
                    temp.append(tree+1)
                else:
                    # 양분 부족하면 여름 양분이 됨
                    die += int(tree / 2)
            # 모든 나무 다 크면 배열 갱신
            arr[r][c] = temp
            # 여름
            nut[r][c] += die

    # 가을
    for r in range(N):
        for c in range(N):
            # 자식이 만들어지면
            if 0 < child[r][c]:
                # 그 수
                cnt = child[r][c]
                # 주변에
                for dr, dc in around:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        for _ in range(cnt):
                            # 나이 1 자식 추가
                            arr[nr][nc].appendleft(1)
                child[r][c] = 0

    # 겨울
    for r in range(N):
        for c in range(N):
            # 양분 추가
            nut[r][c] += A[r][c]

# 최후에 각 위치 배열 길이만큼 나무가 있다.
result = 0
for r in range(N):
    for c in range(N):
        result += len(arr[r][c])

print(result)