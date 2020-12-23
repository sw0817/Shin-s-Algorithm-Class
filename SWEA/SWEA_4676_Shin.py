# SWEA 4676 늘어지는 소리 만들기
# SWEA 4676

# Created by sw0817 on 2020. 12. 23..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRKWITqfvIDFAV8&categoryId=AWRKWITqfvIDFAV8&categoryType=CODE

T = int(input())

for tc in range(1, T+1):
    text = list(input())
    H = int(input())
    locate = list(map(int, input().split()))
    result = ''
    visited = [0] * (len(text)+1)
    for i in range(H):
        visited[locate[i]] += 1

    for i in range(len(text)):
        result += '-' * visited[i]
        result += text[i]

    result += '-' * visited[-1]

    print('#{} {}'.format(tc, result))