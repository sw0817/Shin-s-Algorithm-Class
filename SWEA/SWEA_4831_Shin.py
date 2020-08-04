# SWEA 4831 전기버스
# SWEA 4831

# Created by sw0817 on 2020. 08. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


# 테스트 케이스 수를 받는다.
T = int(input())
# 테스트 케이스마다 반복되는 로직
for tc in range(1, T + 1):
    # K, N, M의 리스트 생성
    KNM = list(map(int, input().split()))
    # 정류장 위치를 나타내는 리스트 생성
    bus_stop = list(map(int, input().split()))

    # 충전횟수와 버스의 초기위치 설정
    charge = 0
    locate = 0
    # K에 따른 버스의 위치 값에 더할 인자 초기 설정
    plus_locate = 0
    # 버스의 위치가 종점 N보다 작은 위치인 동안 반복
    while locate < KNM[1]:
        # 종점부터 초기위치 거리가 이동가능거리 이하면 충전할 필요 없으므로
        # 반복문 탈출
        if KNM[1] - locate <= KNM[0]:
            break

        # 이동가능거리 범위에서 반복문을 돌려 버스위치 + 이동거리가
        # 정류장위치와 같다면 plus_locate 생성. 이때,
        # 충전횟수를 최소화하기 위해 i값이 가장 큰 plus_locate를 찾는다.
        for i in range(KNM[0]):
            if (locate + i + 1) in bus_stop:
                plus_locate = i + 1

        # plus_locate == 0의 의미는 이동범위 내에 충전소가 없다는 뜻
        # 그러므로 0을 출력할 수 있도록 charge = 0
        if plus_locate == 0:
            charge = 0
            break

        # 탈출하지 않고 반복문을 통과했다면 충전 1번을 추가.
        # 버스 위치는 이동거리를 더한 값이 되고,
        # 이동거리는 다시 0으로 초기화한다.
        charge += 1
        locate += plus_locate
        plus_locate = 0

    # 출력
    print('#{} {}'.format(tc, charge))





