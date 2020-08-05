# SWEA 4837 부분집합의 합
# SWEA 4837

# Created by sw0817 on 2020. 08. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = len(A)
    result = 0
    # 부분집합 모두 구현
    for i in range(1 << n):
        jip = []
        # 모든 부분집합의 원소를 빈 리스트에 넣는다.
        for j in range(n):
            if i & (1 << j):
                jip.append(A[j])
        print(jip)
    #     # 리스트의 길이(원소의 갯수)가 N일 때,
    #     if len(jip) == N:
    #         sum_zip = 0
    #         # 모든 원소의 합을 구하고
    #         for k in jip:
    #             sum_zip += k
    #         # 합이 K일 때
    #         if sum_zip == K:
    #             # 가짓수 증가
    #             result += 1

    # print('#{} {}'.format(tc, result))
