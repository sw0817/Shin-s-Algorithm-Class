# 백준 1083 소트
# Baekjoon 1083

# Created by sw0817 on 2021. 04. 22..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1083

# 버블정렬을 이용

N = int(input())
arr = list(map(int, input().split()))
cnt = int(input())

# 반복이 끝나는 것은 교환을 더 이상 할 수 없을 때
for i in range(N-1):
    if cnt == 0:
        break

    max_num = arr[i]
    idx = i
    for j in range(i+1, min(N, i+1+cnt)):
        if max_num < arr[j]:
            max_num = arr[j]
            idx = j

    cnt -= idx - i

    for j in range(idx, i, -1):
        arr[j] = arr[j-1]

    arr[i] = max_num

print(' '.join(map(str, arr)))