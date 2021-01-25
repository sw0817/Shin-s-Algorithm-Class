# 백준 1038 감소하는 수
# Baekjoon 1038

# Created by sw0817 on 2021. 01. 25..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1038

def find(l, num):
    global cnt, is_done

    # 목표 길이면 감소하는 수임. 갯수 증가.
    if l == len(num):
        cnt += 1

        # 목표치 도달했으면 그 감소하는 수 출력
        if cnt == N:
            print(num)
            is_done = 1
            return

    else:
        # 아직 빈 문자열이면 마지막 수가 없음.
        if len(num) == 0:
            for i in range(l-1, 10):
                num = str(i)
                find(l, num)
                num = ''
        else:
            # 마지막 숫자보다 작은 수들 다 붙일 수 있다.
            for i in range(int(num[-1])):

                # 근데 만들 숫자 길이만큼 갈 수 없는 수가 마지막 수면 탐색 중지
                if i < l - len(num) - 1:
                    continue

                # 그게 아니면 만든 숫자로 다시 탐색
                else:
                    num += str(i)
                    find(l, num)
                    num = num[:-1]


N = int(input())

# N이 10보다 작으면 그냥 N이 N번째 감소하는 수.
if N < 10:
    print(N)

else:
    # 9까지는 세고 시작
    cnt = 9
    is_done = 0

    # 원래는 return 하면 거기서 출력하고 프로그램 끝내야 하는데..
    for i in range(2, 11):
        if not is_done:
            find(i, '')

    # 최악의 경우에도 시간 통과 해야하니까 뭐.
    if not is_done:
        print(-1)