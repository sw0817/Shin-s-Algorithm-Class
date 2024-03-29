# 백준 14500 테트로미노
# Baekjoon 14500

# Created by sw0817 on 2021. 12. 14..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14500

# 모든 테트로미노 모양 배열
tetromino = [
    [
        [1, 1, 1, 1],
    ],
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [1, 1],
        [1, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0]
    ],
    [
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 0, 0],
        [1, 1, 1]
    ],
    [
        [0, 1, 0],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 1]
    ],
    [
        [1, 1],
        [1, 0],
        [1, 0]
    ],
    [
        [1, 0],
        [1, 0],
        [1, 1]
    ],
    [
        [1, 1],
        [0, 1],
        [0, 1]
    ],
    [
        [0, 1],
        [0, 1],
        [1, 1]
    ],
    [
        [0, 1],
        [1, 1],
        [0, 1]
    ],
    [
        [1, 0],
        [1, 1],
        [1, 0]
    ],
    [
        [0, 1],
        [1, 1],
        [1, 0]
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1]
    ],
]

N, M = map(int, input().split())

# 테트로미노 모양이 4x4 까지 있으므로 우측, 하단에 길이 3만큼 0포인트 배열 추가
arr = []
for _ in range(N):
    row = list(map(int, input().split())) + [0, 0, 0]
    arr.append(row)
for _ in range(3):
    arr.append([0] * (M+3))

result = 0
for i in range(N):
    for j in range(M):
        # 모든 위치에서 모든 테트로미노에 대해 발생하는 점수 탐색
        for tet in tetromino:
            r, c = len(tet), len(tet[0])
            cur = 0
            for nr in range(r):
                for nc in range(c):
                    cur += arr[i+nr][j+nc] * tet[nr][nc]
            result = max(result, cur)

print(result)