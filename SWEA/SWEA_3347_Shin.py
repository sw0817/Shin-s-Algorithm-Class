# SWEA 3347 올림픽 종목 투표
# SWEA 3347

# Created by sw0817 on 2020. 12. 30..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWDTHsZ6r0EDFAWD&categoryId=AWDTHsZ6r0EDFAWD&categoryType=CODE

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    visited = [0] * N

    for i in range(M):
        for j in range(N):
            if A[j] <= B[i]:
                visited[j] += 1
                break

    result = visited.index(max(visited))+1
    print('#{} {}'.format(tc, result))