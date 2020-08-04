# SWEA 4828 Min Max
# SWEA 4828

# Created by sw0817 on 2020. 08. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


# 테스트 케이스 수를 받는다.
T = int(input())
# 테스트 케이스마다 반복되는 로직
for tc in range(1, T+1):
    # 각 케이스의 양수의 갯수 N 결정
    N = int(input())
    # 주어지는 양수의 리스트를 만든다.
    num_list = list(map(int, input().split()))
    # 최종 계산에 활용될 min, max 값 초기설정
    # (반복문을 이용할 것이기 때문에 초기엔 0번째 인자가 최소값이자 최대값)
    num_min = num_list[0]
    num_max = num_list[0]
    # 주어진 양수 리스트의 각 인자를 반복문으로 돌며 최소값과 최대값을 갱신한다.
    for num in num_list:
        if num < num_min:
            num_min = num
        if num > num_max:
            num_max = num
    # 최대값 - 최소값을 format 함수를 이용해 출력
    print('#{} {}'.format(tc, num_max - num_min))