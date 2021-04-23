# 백준 17825 주사위 윷놀이
# Baekjoon 17825

# Created by sw0817 on 2021. 04. 23..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/17825

# marker, cnt, result, state
def dice(m, c, r, s):
    global result
    # 재귀이므로 상태는 copy해서 사용
    state = s.copy()
    # 주사위 10번 = 0~9
    num = nums[c] - 1
    # 선택된 말의 현재 위치
    state[m] = markList[state[m]][num]
    # 현재 위치 점수
    score = scoreList[state[m]]

    # 10번 다 던진거면
    if c == 9:
        # 갱신
        result = max(result, r + score)
        return

    # 다음 주사위
    # markList 배열 내 위치배열 길이 5 = 0~4
    next_num = nums[c+1] - 1

    # 모든 말에 대해
    for i in range(4):
        # 도착한 말이면 넘어가기
        # 도착점이 아닌데 다른 말이랑 겹쳐도 넘어가기
        if state[i] == 32 or markList[state[i]][next_num] != 32 and markList[state[i]][next_num] in state:
            continue

        # 위에서 안 걸렸으면 해당 말 움직여보기
        dice(i, c+1, r + score, state)


# 시작점부터 각각 위치에서 갈 수 있는 위치 번호 집합
# 시작점은 0, 도착점은 32
markList = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8],
    [5,6,7,8,9],
    [21,22,23,29,30],
    [7,8,9,10,11],
    [8,9,10,11,12],
    [9,10,11,12,13],
    [10,11,12,13,14],
    [24,25,29,30,31],
    [12,13,14,15,16],
    [13,14,15,16,17],
    [14,15,16,17,18],
    [15,16,17,18,19],
    [26,27,28,29,30],
    [17,18,19,20,32],
    [18,19,20,32,32],
    [19,20,32,32,32],
    [20,32,32,32,32],
    [32,32,32,32,32],
    [22,23,29,30,31],
    [23,29,30,31,20],
    [29,30,31,20,32],
    [25,29,30,31,20],
    [29,30,31,20,32],
    [27,28,29,30,31],
    [28,29,30,31,20],
    [29,30,31,20,32],
    [30,31,20,32,32],
    [31,20,32,32,32],
    [20,32,32,32,32]
]
# 위치 당 점수
scoreList = [0] + [i*2 for i in range(1, 21)] + [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]
# 주사위 눈
nums = list(map(int, input().split()))
result = 0
# 처음 말 위치
marker = [0, 0, 0, 0]
dice(0, 0, 0, marker)
print(result)