# 프로그래머스 84325 직업군 추천하기
# Programmers 84325

# Created by sw0817 on 2021. 08. 25..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    answer = []
    l = len(languages)
    new_table = []
    result = [0] * 5
    for i in range(5):
        temp = list(table[i].split())
        new_table.append(temp)
        for j in range(l):
            if languages[j] in temp:
                result[i] += preference[j] * ((temp.index(languages[j]) - 6) * -1)

    max_point = 0
    for i in range(5):
        if max_point == result[i]:
            answer.append(new_table[i][0])
        elif max_point < result[i]:
            max_point = result[i]
            answer = [new_table[i][0]]

    answer.sort()

    return answer[0]