# SWEA 2001 파리 퇴치
# SWEA 2001

# Created by sw0817 on 2020. 08. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 테스트케이스 별 파리 분포 2차원 배열 생성
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    # 최대 파리 잡는 수 초기설정
    max_flies = 0
    # 파리채 범위를 고려해 검색할 영역의 길이를 결정
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 시행 당 파리 잡는 수는 0으로 갱신
            pre_flies = 0
            # 파리채 크기만큼 영역 설정
            for k in range(M):
                for l in range(M):
                    # 검색점에서 파리채 영역만큼 분포하는 파리의 개체 수를 합
                    pre_flies += arr[i+k][j+l]
            # 최대 값보다 시행값이 크다면 최대값 갱신
            if pre_flies > max_flies:
                max_flies = pre_flies

    print('#{} {}'.format(tc, max_flies))