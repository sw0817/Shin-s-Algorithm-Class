# SWEA 1486 장훈이의 높은 선반
# SWEA 1486

# Created by sw0817 on 2020. 09. 17..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw&categoryId=AV2b7Yf6ABcBBASw&categoryType=CODE


def subset(k, n, cur_sum):
    global mini
    if k == n:
        if cur_sum - B < mini and cur_sum >= B:
            mini = cur_sum - B
        return
    else:
        bits[k] = 1 # k 번 요소에 대한 선택을 저장
        A.append(H[k])
        subset(k + 1, n, cur_sum + H[k])
        A.pop()     # k 번 요소 넣고 새로운 함수 갔으니까 빼줘야지

        bits[k] = 0
        subset(k + 1, n, cur_sum) # k번 요소를 포함하지 않는다.


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    A = []
    bits = [0] * N
    mini = sum(H)
    subset(0, N, 0)
    print(mini)