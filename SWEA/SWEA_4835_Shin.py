# SWEA 4835 구간합
# SWEA 4835

# Created by sw0817 on 2020. 08. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


# 테스트 케이스 수를 받는다.
T = int(input())
# 테스트 케이스마다 반복되는 로직
for tc in range(1, T+1):
    # N개의 정수 배열 M개의 합 N, M 리스트
    NM = list(map(int, input().split()))
    # N개의 정수 리스트 설정.
    num_list = list(map(int, input().split()))
    # 초기 최소, 최대값 설정. 최소값은 N의 최대값 10000 * N의 최대 갯수 100개 의 합 이상으로 설정
    num_min = 10000 * 100
    num_max = 0
    # 구간 합의 갯수는 N-M+1 개
    for i in range(0, NM[0]-NM[1]+1):
        # 구간의 초기합과 반복문 속 구간합
        N_sum = 0
        for j in range(NM[1]):
            N_sum += num_list[i+j]
        # 구간합이 최대합보다 큰 경우와 최소합보다 작은 경우 갱신
        if N_sum > num_max:
            num_max = N_sum
        if N_sum < num_min:
            num_min = N_sum

    print('#{} {}'.format(tc, num_max - num_min))



