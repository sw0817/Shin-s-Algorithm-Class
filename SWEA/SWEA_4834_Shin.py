# SWEA 4834 숫자 카드
# SWEA 4834

# Created by sw0817 on 2020. 08. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


# 테스트 케이스 수를 받는다.
T = int(input())
# 테스트 케이스마다 반복되는 로직
for tc in range(1, T+1):

    # 숫자 카드의 수 N
    N = int(input())
    # 카드의 리스트 설정
    cards = list(map(int, str(input())))
    # 가장 많은 카드의 개수, 그 카드의 숫자 초기값 설정
    cnt_max = 0
    num_max = 0
    # 모든 카드에 대해서 다른 카드와 비교
    for i in range(N):
        # 비교하는 카드의 개수와 최대값을 비교하기 위한 변수 설정
        cnt = 0
        # 앞서 비교한 카드는 중복해서 비교할 필요 없기 때문에 제외하고 비교할 수 있도록 range 설정
        for j in range(i, N):
            # 같은 카드인 경우 cnt += 1
            if cards[i] == cards[j]:
                cnt += 1
        # i 카드의 모든 다른 카드와 비교가 끝났을 때, 카드의 개수를 최대값과 비교해 갱신
        if cnt >= cnt_max:
            cnt_max = cnt
            # 최대개수 값으로 갱신된 카드인 경우, 카드 자체의 숫자 크기를 최대 숫자크기값과 비교
            if num_max <= cards[i]:
                num_max = cards[i]
# 출력
    print('#{} {} {}'.format(tc, num_max, cnt_max))