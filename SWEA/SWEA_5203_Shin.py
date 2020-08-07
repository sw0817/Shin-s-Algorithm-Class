# SWEA 5203 베이비진 게임
# SWEA 5203

# Created by sw0817 on 2020. 08. 07..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


# 원소수가 3개인 부분집합을 생성
# 1이 3개인 6자리 2진수 --> 0도 3개
cards = [5,4,1,2,3,6]

for subset in range(1 << 6):
#cards.sort()
    A, B = [], []
    for i in range(6):
        if subset & (1 << i):
            A.append(cards[i])
        else:
            B.append(cards[i])

    if len(A) == len(B):
        print(A, B)

# 부분집합과 조합은 관계가 있구나.