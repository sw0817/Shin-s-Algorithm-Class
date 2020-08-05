# SWEA 4843 특별한 정렬
# SWEA 4843

# Created by sw0817 on 2020. 08. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    result = []
    # 주어진 정수를 모두 빈 리스트에 넣을 때까지 반복
    while N_list != []:
        # 첫 인자를 최소값과 최대값으로 초기설정
        max_N = N_list[0]
        min_N = N_list[0]
        # 모든 인자를 확인해서 최소값과 최대값 갱신
        for num in N_list:
            if num > max_N:
                max_N = num
            if num < min_N:
                min_N = num
        # 최대값, 최소값 순으로 결과리스트에 넣고 주어진 리스트에서는 삭제
        result.append(max_N)
        result.append(min_N)
        N_list.remove(max_N)
        N_list.remove(min_N)

    print('#{}'.format(tc), end=' ')
    # 10개만 출력
    for i in range(10):
        print(result[i], end=' ')
    print()