# SWEA 1258 행렬찾기
# SWEA 1258

# Created by sw0817 on 2020. 08. 09..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN&categoryId=AV18LoAqItcCFAZN&categoryType=CODE


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 테스트케이스별 전체행렬 생성
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))

    # 부분 행렬을 정리할 최종 리스트 초기생성
    result_list = []


    # 2차원 배열을 왼쪽 위에서부터 오른쪽 아래로 검색하며,
    # 0이 아닌 숫자를 찾는다.
    for i in range(n):
        for j in range(n):
            # 0이 아닌 값을 만나면, 그 값으로부터, 오른쪽과 아래로
            # 몇개의 숫자가 0이 아닌 숫자인지 검색한다.
            if mat[i][j] != 0:
                # 부분행렬의 가로세로 길이를 저장할 빈 리스트 생성
                pre_list = []
                cnt_j = 1
                cnt_i = 1
                # 오른쪽 길이를 잰다.
                for k in range(j+1, n):
                    if mat[i][k] != 0:
                        cnt_j += 1
                    # 0을 만나면 길이 측정 중단.
                    else:
                        break

                # 아래쪽 길이를 잰다.
                for l in range(i+1, n):
                    if mat[l][j] != 0:
                        cnt_i += 1
                    # 역시 0을 만나면 길이 측정 중단.
                    else:
                        break

                # 측정된 길이를 이용해, 사각형 모양으로 숫자를
                # 0으로 치환한다.
                for k in range(i, i+cnt_i):
                    for l in range(j, j+cnt_j):
                        mat[k][l] = 0

                # 측정된 가로 세로 길이를 갱신하기 전에
                # 리스트로 묶고, 그 리스트를 최종 리스트에 넣는다.
                pre_list.append(cnt_i)
                pre_list.append(cnt_j)
                result_list.append(pre_list)

    # 최종 리스트의 길이 = 부분행렬의 갯수
    N = len(result_list)

    # 최종 리스트 인자의 곱의 값을 오름차순으로 정렬
    for i in range(0, N - 1):
        idx = i
        for j in range(i + 1, N):
            if result_list[idx][0] * result_list[idx][1] > result_list[j][0] * result_list[j][1]:
                idx = j

        result_list[i], result_list[idx] = result_list[idx], result_list[i]

    # 출력.
    print('#{} {}'.format(tc, N), end=' ')
    for i in range(N):
        print('{} {}'.format(result_list[i][0], result_list[i][1]), end=' ')
    print()