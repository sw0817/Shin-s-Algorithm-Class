# SWEA 4013 특이한 자석
# SWEA 4013

# Created by sw0817 on 2020. 10. 22..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH&categoryId=AWIeV9sKkcoDFAVH&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    turns = [list(map(int, input().split())) for _ in range(K)]
    score = 0
    for turn in turns:
        num = turn[0]-1
        dir = turn[1]

        rotations = [(num, dir)]

        temp = dir
        for i in range(num-1, -1, -1):
            if magnetics[i][2] != magnetics[i+1][6]:
                temp *= -1
                rotations.append((i, temp))
            else:
                break

        temp = dir
        for i in range(num+1, 4):
            if magnetics[i][6] != magnetics[i-1][2]:
                temp *= -1
                rotations.append((i, temp))
            else:
                break

        for num, dir in rotations:
            if dir == 1:
                magnetics[num].insert(0, magnetics[num].pop())
            else:
                magnetics[num].append(magnetics[num].pop(0))

    for i in range(4):
        if magnetics[i][0] == 1:
            score += 2 ** i

    print('#{} {}'.format(tc, score))