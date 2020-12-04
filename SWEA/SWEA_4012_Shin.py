# SWEA 4012 요리사
# SWEA 4012

# Created by sw0817 on 2020. 12. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

# 두 그룹의 선정을 위해 조합을 사용한다.
from itertools import combinations


T = int(input())

for tc in range(1, T+1):

    # 재료의 수
    N = int(input())

    # 시너지 표
    foods = [list(map(int ,input().split())) for _ in range(N)]

    # 최소값 초기화
    result = 999999 ** 2

    # 그룹 선정을 위한 idx 배열
    nums = [i for i in range(N)]

    # 재료(idx를 가진)를 반 가지는 조합의 배열
    # 이 배열은 중앙을 기준으로 대칭되어 인자를 나누어 가진다.
    # (0번째 조합과 -1번째 조합의 인자는 모두 다르다.)
    nums_com = list(combinations(nums, N//2))

    # 중앙에서 대칭되기에 반만 조사하면 모든 케이스를 조사할 수 있다.
    for i in range(len(nums_com)//2):

        # 나누어진 조합 시너지 합
        A_sum = 0
        B_sum = 0

        # 조합의 시너지 값을 구한다.
        for j in range(N//2-1):

            # 자신을 제외하고 다음 인자들과 시너지를 구하면 모두 조사 가능
            for k in range(j+1, N//2):
                A_sum += foods[nums_com[i][j]][nums_com[i][k]]
                A_sum += foods[nums_com[i][k]][nums_com[i][j]]

        for j in range(N//2-1):
            for k in range(j+1, N//2):
                B_sum += foods[nums_com[len(nums_com)-1-i][j]][nums_com[len(nums_com)-1-i][k]]
                B_sum += foods[nums_com[len(nums_com)-1-i][k]][nums_com[len(nums_com)-1-i][j]]

        # 구해진 각 시너지 합의 차이를 최소값과 비교
        if result > abs(A_sum-B_sum):
            result = abs(A_sum-B_sum)

    print('#{} {}'.format(tc, result))
