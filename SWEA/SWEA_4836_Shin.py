# SWEA 4836 색칠하기
# SWEA 4836

# Created by sw0817 on 2020. 08. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


T = int(input())
for tc in range(1, T+1):
    # 결과값 초기설정
    result = 0
    # 기본 2차원 index 모두 0으로 초기설정
    arr = [[0 for i in range(10)] for j in range(10)]
    # 조건 개수
    t = int(input())
    # 조건 2차원 리스트 생성
    pre_list = []
    for i in range(t):
        pre_list.append(list(map(int, input().split())))
    # 빨강 칠해지는 index 값이 1이 아니면 1을 더하고
    # 파랑 칠해지는 index 값이 2가 아니면 2를 더함
    for i in range(len(pre_list)):
        for j in range(pre_list[i][0], pre_list[i][2]+1):
            for k in range(pre_list[i][1], pre_list[i][3]+1):
                if pre_list[i][4] == 1:
                    if arr[j][k] != 1:
                        arr[j][k] += pre_list[i][4]
                else:
                    if arr[j][k] != 2:
                        arr[j][k] += pre_list[i][4]

    # index 재검색 했을 때, 값이 3이면 보라색
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                result += 1

    print('#{} {}'.format(tc, result))
