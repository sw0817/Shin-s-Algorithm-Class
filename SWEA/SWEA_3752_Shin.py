# SWEA 3752 가능한 시험 점수
# SWEA 3752

# Created by sw0817 on 2020. 10. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn&categoryId=AWHPkqBqAEsDFAUn&categoryType=CODE


T = int(input())

for tc in range(1, T+1):
    
    N = int(input())
    scores = list(map(int, input().split()))
    visited = [1] + [0] * sum(scores)
    result = [0]
    for score in scores:
        for i in range(len(result)):
            if visited[score+result[i]] == 0:
                visited[score+result[i]] = 1
                result.append(score+result[i])

    print('#{} {}'.format(tc, len(result)))
