# SWEA 5550 나는 개구리소이다
# SWEA 5550

# Created by sw0817 on 2020. 10. 18..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWxqfhKAWgDFAW4&categoryId=AWWxqfhKAWgDFAW4&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    # 개구리 울음소리
    sound = input()
    # 정상적인 울음소리는 croak

    # 리스트로 변환
    sound_list = list(sound)

    # 각 울음소리를 숫자로 변환
    for i in range(len(sound_list)):
        if sound_list[i] == 'c':
            sound_list[i] = 1
        elif sound_list[i] == 'r':
            sound_list[i] = 2
        elif sound_list[i] == 'o':
            sound_list[i] = 3
        elif sound_list[i] == 'a':
            sound_list[i] = 4
        else:
            sound_list[i] = 5

    # 현재 위치(index)
    temp = 0
    # 시작은 c
    check = 1

    # 울음소리의 첫 시작이 c가 아니면 불가능하다
    if sound_list[0] != 1:
        min_num = -1

    # 최소 개구리 수
    min_num = 0
    # 순간 개구리 수
    cnt = 0

    # 현재 울음소리 위치가 마지막이기 전까지
    while temp < len(sound_list):
        # k가 나오기 전까지 c의 갯수는 최소 개구리 수
        if sound_list[temp] == 1:
            cnt += 1

        # 현재 체크하고 있는 소리가 나오면 0으로 치환하여 개구리가 정상적으로
        # 소리를 내는지 판단한다.
        if check == sound_list[temp]:
            check += 1
            sound_list[temp] = 0

            # k까지 소리를 냈다면
            if check == 6:
                # 지금 까지 최소 개구리 수가 최대값인지 확인
                if cnt > min_num:
                    min_num = cnt

                # 현재 위치가 마지막 소리면 더 이상 k가 없으므로 반복문 탈출
                if temp == len(sound_list)-1:
                    break

                # 다시 c를 확인해야하고
                check = 1
                # 처음부터 확인한다.
                temp = 0
                # 순간 개구리 수 초기화
                cnt = 0
                continue
        # 현재 확인하는 소리가 아니라면
        else:
            # 전과 같은 소리거나 지금 확인하는 소리가 아니면 비정상적인 소리임
            if check + 1 < sound_list[temp]:
                break
        # 다음 위치로
        temp += 1

    # 모든 소리를 정상적으로 확인하여 0으로 치환해야 정상적 소리이므로
    # 합이 0이 아니라면 비정상
    # 또는 마지막을 k로 마치지 않았다면 비정상
    if sum(sound_list) > 0 or check != 6:
        min_num = -1


    print('#{} {}'.format(tc, min_num))
