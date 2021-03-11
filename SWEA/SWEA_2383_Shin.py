# SWEA 2383 점심 식사시간
# SWEA 2383

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl&categoryId=AV5-BEE6AK0DFAVl&categoryType=CODE&problemTitle=%EC%A0%90%EC%8B%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 배열, 사람, 문 위치 모두 확인
    arr = []
    people = []
    door = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] == 1:
                people.append((i, j))
            elif row[j] >= 2:
                door.append((i, j, row[j]))
        arr.append(row)

    # 사람 수 이자 사람 배열 길이
    P = len(people)

    # 대충 큰 시간 초기값
    t = 9999999999

    # 부분집합 쓸거라 만드는 배열(사실 combination 썼었는데 사용 불가능이라 바꿈,,)
    idx = [i for i in range(P)]

    # 각 사람 문1, 문2 까지 거리 배열
    length = [[0, 0] for _ in range(P)]

    left_time = door[0][2]
    right_time = door[1][2]

    # 문 좌표
    # 이건 생각해보니까 처음에 배열에 저장하는게 편했을 듯
    dx1, dy1, dx2, dy2 = door[0][0], door[0][1], door[1][0], door[1][1]

    # 모든 사람에 대해 문 거리 배열 채워준다.
    for i in range(P):
        px, py = people[i]
        length[i][0] = abs(px-dx1) + abs(py-dy1)
        length[i][1] = abs(px-dx2) + abs(py-dy2)

    # 부분 집합 만들어서 그걸 왼쪽으로 칭함 (왼쪽 문 갈 사람 정하기)
    for i in range(P << 2):
        left = []
        for j in range(P):
            if i & (1 << j):
                left.append(idx[j])

        # 왼쪽, 오른쪽 문 배열
        ld = []
        rd = []
        for j in range(P):

            # 왼쪽 가는 애들은 왼쪽문 거리 추가 오른쪽은 오른쪽 거리 추가
            if j in left:
                ld.append(length[j][0])
            else:
                rd.append(length[j][1])

        # 거리 짧은 순으로 소팅
        ld.sort()
        rd.sort()

        # 왼쪽, 오른쪽 모두 탈출하는 시간
        left_t = 0
        right_t = 0

        # 각각 큐 생성해서 3명씩 넣어줘야함

        while ld:
            time = ld.pop(0)
            # 현재 시간보다 젤 빠른 도착시간이 크면 탈출 시간까지 합쳐서
            # 현재시간 갱신
            if left_t < time:
                left_t = time + left_time

            # 이미 도착했으면 탈출 시간만 추가
            else:
                left_t = time + left_time

        # 오른쪽도 마찬가지
        while rd:
            time = rd.pop(0)
            if right_t < time:
                right_t = time + right_time
            else:
                right_t = time + right_time

        # 왼쪽 오른쪽 중 오래걸리는게 최종 탈출 시간
        result_t = max(left_t, right_t)

        # 그것들 중 젤 빠른걸로 갱신
        if result_t < t:
            t = result_t

    print("#{} {}".format(tc, t))