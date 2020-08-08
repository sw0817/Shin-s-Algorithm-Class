# SWEA 1974 스도쿠 검증
# SWEA 1974

# Created by sw0817 on 2020. 08. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE


# 중간에 스도쿠검증에 실패하면 0을 return 하고 검증을 멈추기 위해
# 함수를 정의
def sdoku(list):
    # i가 바뀔때마다 가로와 세로의 스도쿠를 검증하기위해 리스트 생성
    for i in range(9):
        x_list = []
        y_list = []
        for j in range(9):
            # j가 바뀔때마다 가로와 세로의 검증 리스트 인자를 추가
            x_list.append(list[i][j])
            y_list.append(list[j][i])
            # 3x3 사각형 스도쿠 검증을 위한 리스트 j가 바뀔때마다 생성
            squ_list = []
            # 3x3이므로 k, l은 범위가 0,1,2
            for k in range(3):
                for l in range(3):
                    # 사각형은 모든 [i][j]로부터가 아니라 3칸씩 떨어져
                    # 생성
                    if i % 3 == 0 and j % 3 == 0:
                        squ_list.append(list[i+k][j+l])
            # 그때, 모든 인자가 추가된 리스트에서 겹치는 숫자가 있는지 확인
            if i % 3 == 0 and j % 3 == 0:
                for n in range(8):
                    for m in range(n+1, 9):
                        # 겹치는 숫자가 있다면 검증 실패
                        if squ_list[n] == squ_list[m]:
                            return 0
        # 가로 세로도 마찬가지로 겹치는 숫자가 있다면 검증 실패
        for n in range(8):
            for m in range(n + 1, 9):
                if x_list[n] == x_list[m] or y_list[n] == y_list[m]:
                    return 0
    # 검증을 실패하지 않고 함수 끝까지 나온다면, 가로세로 사각형에
    # 겹치는 숫자가 없다는 의미이고, 숫자는 1~9 에서만 생성되므로,
    # 9칸에 겹치는 숫자가 없다면 스도쿠이다.
    return 1

T = int(input())
for tc in range(1, T+1):
    sdo_list = []
    for i in range(9):
        sdo_list.append(list(map(int, input().split())))


    print('#{} {}'.format(tc, sdoku(sdo_list)))

