# SWEA 5203 베이비진 게임
# SWEA 5203

# Created by sw0817 on 2020. 10. 30..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def baby_gin():
    global result
    for i in range(len(card_set)):
        if i % 2 == 0:
            player1[card_set[i]] += 1
            if player1[card_set[i]] == 3:
                result = 1
                return
            else:
                check = 0
                for j in range(card_set[i] - 2, card_set[i] + 3):
                    if j < 0 or 10 <= j:
                        continue
                    else:
                        if player1[j] > 0:
                            check += 1
                            if check == 3:
                                result = 1
                                return
                        else:
                            check = 0

        else:
            player2[card_set[i]] += 1
            if player2[card_set[i]] == 3:
                result = 2
                return
            else:
                check = 0
                for j in range(card_set[i] - 2, card_set[i] + 3):
                    if j < 0 or 10 <= j:
                        continue
                    else:
                        if player2[j] > 0:
                            check += 1
                            if check == 3:
                                result = 2
                                return
                        else:
                            check = 0


T = int(input())
for tc in range(1, T+1):
    card_set = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    result = 0
    baby_gin()
    print('#{} {}'.format(tc, result))