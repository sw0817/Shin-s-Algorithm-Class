# SWEA 1208 Flatten
# SWEA 1208

# Created by sw0817 on 2020. 08. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE


# input 코드에 T는 주어지지 않고 10으로 정해져있다.
T = 10 # 원래라면 T = int(input())
# 테스트 케이스마다 반복되는 로직
for tc in range(1, T+1):
    # input으로 받는 덤프 횟수와 상자위치 리스트
    dump = int(input())
    num_list = list(map(int, input().split()))
    # 덤프 횟수를 모두 소진해 0이 될 때까지 반복.
    while dump > 0:
        # 박스 높이의 최댓값과 최솟값을 첫 줄의 박스 높이로 초기설정
        num_max = num_list[0]
        num_min = num_list[0]
        # 모든 박스 높이를 대조해 최댓값과 최솟값 갱신
        for num in num_list:
            if num > num_max:
                num_max = num
            if num < num_min:
                num_min = num
        # 가로길이는 항상 100
        for j in range(len(num_list)):
            # 반복문 중 박스 높이가 최댓값과 같다면 그 줄의 상자를 하나 제거
            if num_list[j] == num_max:
                num_list[j] -= 1
                # 그 때, 다시 박스 높이가 최솟값과 같은 줄을 찾아 상자를 하나 추가
                for i in range(len(num_list)):
                    if num_list[i] == num_min:
                        num_list[i] += 1
                # 2중 for 반복문을 모두 break 하여 같은 높이의 다른 줄에는 영향 X
                        break
                break
        # 상자가 이동했으므로 덤프 횟수 1 소진
        dump -= 1
    # 옮겨진 상자 더미의 높이 최솟값과 최댓값을 다시 첫번째 줄 높이로 초기화
    num_max = num_list[0]
    num_min = num_list[0]
    # 모든 줄의 상자 높이를 탐색해 최댓값과 최솟값 갱신
    for num in num_list:
        if num >= num_max:
            num_max = num
        if num <= num_min:
            num_min = num
    # 최댓값과 최솟값의 차를 result 로 정했음
    result = num_max - num_min
    # 출력
    print('#{} {}'.format(tc, result))