# SWEA 4838 이진탐색
# SWEA 4838

# Created by sw0817 on 2020. 08. 05..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


# 이진탐색 함수를 생성
def find_c(end, c):
    result = 0
    l = 1
    while l <= end:
        # 중앙값 갱신시마다 탐색횟수 1 증가
        middle = (l + end) // 2
        result += 1
        # 중앙값이 찾을 값과 같으면 탐색횟수 리턴
        if middle == c:
            return result
        # 중앙값이 작으면 탐색 시작값을 중앙값으로 갱신
        elif middle < c:
            l = middle
        # 중앙값이 크면 탐색 끝값을 중앙값으로 갱신
        else:
            end = middle


T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())


    Pan = find_c(P, Pa)
    Pbn = find_c(P, Pb)

    if Pan > Pbn:
        print('#{} B'.format(tc))
    elif Pbn > Pan:
        print('#{} A'.format(tc))
    else:
        print('#{} 0'.format(tc))