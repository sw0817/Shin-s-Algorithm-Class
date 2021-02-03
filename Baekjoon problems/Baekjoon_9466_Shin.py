# 백준 9466 텀 프로젝트
# Baekjoon 9466

# Created by sw0817 on 2021. 02. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/9466

from _collections import deque


T = int(input())

for tc in range(T):
    n = int(input())
    next = list(map(int, input().split()))

    # 선택된 자들
    selected = [0] * n

    # 차례대로 선택해볼건데
    for i in range(n):

        # 선택된 놈은 제외
        if not selected[i]:

            # num이란 다음 선택할 놈
            num = next[i]-1

            # 자신을 선택했으면
            if num == i:

                # 선택된 자로 가고 다음 놈
                selected[i] = 1
                continue

            # 스택에 시작한 놈 넣고
            stack = deque()
            stack.append(i)

            # 다음 선택할 놈이 스택에 없고 선택도 안 됐으면
            while num not in stack and not selected[num]:

                # 스택에 추가
                stack.append(num)

                # 다음 놈 갱신
                num = next[num]-1

            # 다음 놈이 선택됐거나 해서 혼잔데 자신 선택한게 아니면 넘어가
            if len(stack) == 1 and num != i:
                continue

            # 선택 중인 놈이면
            elif num in stack:

                # 선택 받은 자가 되고
                selected[num] = 1

                # 걔 나올때까지 팝해서 선택 받은자
                while stack and stack[-1] != num:
                    selected[stack.pop()] = 1

    # 답 출력
    print(n-sum(selected))