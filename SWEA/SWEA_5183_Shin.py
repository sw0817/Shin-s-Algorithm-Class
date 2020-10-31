# SWEA 5189 전자카트
# SWEA 5189

# Created by sw0817 on 2020. 10. 31..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


from itertools import permutations


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 100 * N * N
    table = [list(map(int, input().split())) for _ in range(N)]
    nums = list(i for i in range(1, N))
    line = list(permutations(nums, N-1))

    for i in range(len(line)):
        check = 0
        temp = line[i]
        check += table[0][temp[0]]

        for j in range(len(temp)-1):
            check += table[temp[j]][temp[j+1]]

        check += table[temp[j+1]][0]
        if check < result:
            result = check

    print('#{} {}'.format(tc, result))