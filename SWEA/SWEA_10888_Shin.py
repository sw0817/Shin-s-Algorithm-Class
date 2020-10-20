# SWEA 10888 음식배달
# SWEA 10888

# Created by sw0817 on 2020. 10. 20..
# Copyright © 2020 sw0817. All rights reserved.

# See :


from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    # 맵 길이
    N = int(input())
    # 이것보단 비용이 작을 것
    min_sum = N ** 10
    # 맵
    mapp = []
    # 가게들 좌표 리스트
    stores = []
    # 집들 좌표 리스트
    houses = []
    for i in range(N):
        # 한 줄씩 맵에 넣고
        line = list(map(int, input().split()))
        mapp.append(line)
        for j in range(N):
            # 가게 좌표
            if line[j] > 1:
                stores.append((i, j))
            # 집 좌표
            elif line[j] == 1:
                houses.append((i, j))

    # 가게 갯수
    stores_num = len(stores)

    # 가게를 선택할 수 있는 모든 조합
    for i in range(1, stores_num + 1):
        # i 개의 가게를 선택하는 조합
        comb = combinations(stores, i)
        # 의 리스트
        comb_list = list(comb)

        # 그 조합들 중
        for j in range(len(comb_list)):
            # 가장 짧은 거리가 나오는 경우를 선택할건데
            len_sum = 0

            # 모든 집에 대해서
            for house in houses:
                # 각 집의 경우 선택된 조합에 포함된 가게 중 가장 짧은 거리를 구할거야
                min_len = N * N
                # 그리고 선택한 가게의 비용값도 같이 계산해야겠지
                pay = 0
                # 선택된 조합의 모든 가게 중
                for locate in comb_list[j]:
                    # 가게 비용과
                    pay += mapp[locate[0]][locate[1]]
                    # 집으로부터 거리를 구하는데
                    temp = abs(house[0] - locate[0]) + abs(house[1] - locate[1])
                    # 젤 짧은 거리 구해서
                    if min_len > temp:
                        # 갱신
                        min_len = temp
                # 지금 조합에서 선택된 집의 최소거리를 조합거리에 더하자
                len_sum += min_len

            # 조합거리랑 가게비용의 합이 가장 작으면
            if len_sum + pay < min_sum:
                # 갱신
                min_sum = len_sum + pay

    print('#{} {}'.format(tc, min_sum))


