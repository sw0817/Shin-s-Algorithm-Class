# SWEA 4014 활주로 건설
# SWEA 4014

# Created by sw0817 on 2020. 12. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH&categoryId=AWIeW7FakkUDFAVH&categoryType=CODE

T = int(input())

for tc in range(1, T+1):

    # 활주로 길이 N, 경사로 길이 X
    N, X = map(int, input().split())

    # 가능한 경우의 수
    result = 0

    # 활주로 경사 배열
    arr = []

    # 활주로 배열을 추가할 때 가로 활주로 가능성 여부 같이 검사
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

        # 기준 높이 (시작은 0번 인덱스)
        temp = row[0]

        # 경사로를 설치한 곳에 다시 설치할 수 없다.
        visited = [0] * N

        # 세 가지 케이스가 존재. (전보다) 작거나, 같거나, 크거나
        # 현재 idx
        i = 1

        # 경사로 검사 후 확인할 필요 없는 idx 경사를 넘어가기 위해
        # for 문 보다는 while 문이 효율적
        while i < N:

            # 경사 차이가 1보다 크면 방법이 없다.
            if abs(row[i]-temp) > 1:
                break

            # 1. 경사가 1 작아졌을 때
            if row[i] < temp:

                # 불가능 여부
                pos = False

                # 경사로 설치는 필수다.
                visited[i] = 1

                # 현재 위치부터 X 길이의 경사로 설치를 해야함
                for j in range(1, X):

                    # 설치해야 하는 위치가 전체 배열을 벗어나거나
                    # 같은 경사 높이를 가지지 못하면
                    if N <= i+j or row[i+j] != row[i]:

                        # 불가능 여부 True
                        pos = True
                        break

                    # 설치가 되면 설치 표시
                    visited[i+j] = 1

                # 불가능 했다면 이 가로줄 검사는 의미가 없다.
                if pos:
                    break

                # 경사로 설치가 완료됨에 따라 기준 높이는 마지막 높이
                temp = row[i+X-1]

                # 검사할 idx 는 경사로 다음 위치
                i += X

            # 같은 높이라면 검사할 idx 만 증가
            elif row[i] == temp:
                i += 1

            # 높아진다면, 앞에서 경사로를 설치했어야 한다.
            elif temp < row[i]:

                # 불가능 여부
                pos = False

                # 현재 위치 전에 경사로 길이만큼 조사
                for j in range(1, X+1):

                    # 경사로 설치 위치가 배열 바깥이거나
                    # 같이 높이가 아니거나
                    # 이미 경사로가 설치된 자리라면
                    if i-j < 0 or row[i-j] != row[i]-1 or visited[i-j]:

                        # 불가능
                        pos = True
                        break

                # 불가능 여부 확인
                if pos:
                    break

                # 설치가 완료 되었다면 현재 높이가 기준 높이
                temp = row[i]

                # 다음 idx 높이 검사
                i += 1

        # 불가능해서 break 된게 아니라 정상적으로 while 문을 통과했다면
        if N <= i:

            # 경우의 수 증가
            result += 1

    # 세로 방향 동일
    for j in range(N):
        visited = [0] * N
        temp = arr[0][j]

        # 세 가지 케이스가 존재. (전보다) 작거나, 같거나, 크거나
        i = 1
        while i < N:
            if abs(arr[i][j]-temp) > 1:
                break

            if arr[i][j] < temp:
                pos = False
                visited[i] = 1

                for k in range(1, X):

                    if N <= i+k or arr[i+k][j] != arr[i][j]:
                        pos = True
                        break

                    visited[i+k] = 1

                if pos:
                    break

                temp = arr[i+X-1][j]
                i += X

            elif arr[i][j] == temp:
                i += 1

            elif temp < arr[i][j]:
                pos = False

                for k in range(1, X+1):

                    if i-k < 0 or arr[i-k][j] != arr[i][j]-1 or visited[i-k]:
                        pos = True
                        break

                if pos:
                    break

                temp = arr[i][j]
                i += 1

        if N <= i:
            result += 1

    print('#{} {}'.format(tc, result))

