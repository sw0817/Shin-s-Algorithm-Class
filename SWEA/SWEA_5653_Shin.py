# SWEA 5653 벽돌 깨기
# SWEA 5653

# Created by sw0817 on 2020. 12. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo&categoryId=AWXRJ8EKe48DFAUo&categoryType=CODE

nexts = [(1, 0), (0, 1), (-1, 0), (0, -1)]


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    arr = [[0] * (110 + K*2) for _ in range(110 + K*2)]
    arr2 = [[0] * (110 + K*2) for _ in range(110 + K*2)]

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            arr[K+5+i][K+5+j] = row[j]
            arr2[K+5+i][K+5+j] = -row[j]

    t = 0
    stack = []
    while t < K:
        t += 1
        for i in range(110 + K*2):
            for j in range(110 + K*2):
                # 비활성 세포
                if arr[i][j] > 0 and arr[i][j] != 11:
                    if arr2[i][j] < 0:
                        arr2[i][j] += 1
                        if arr2[i][j] == 0:
                            arr2[i][j] = arr[i][j]
                            arr[i][j] = -arr[i][j]


                # 활성 세포
                elif arr[i][j] < 0:
                    if arr[i][j] == -arr2[i][j]:
                        stack.append((-arr[i][j], i, j))
                    if arr2[i][j] > 0:
                        arr2[i][j] -= 1
                        if arr2[i][j] == 0:
                            # stack.append((-arr[i][j], i, j))
                            arr[i][j] = 11

        stack.sort()
        while stack:
            n, r, c = stack.pop()
            for dr, dc in nexts:
                nr = r + dr
                nc = c + dc
                if arr[nr][nc] == 0 and arr2[nr][nc] == 0:
                    arr[nr][nc] = n
                    arr2[nr][nc] = -n

        # for row in arr:
        #     print(row)

    result = 0
    for i in range(110 + K*2):
        for j in range(110 + K*2):
            if arr[i][j] != 0 and arr[i][j] != 11:
                result += 1

    print('#{} {}'.format(tc, result))
