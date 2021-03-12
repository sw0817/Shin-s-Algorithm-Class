# 백준 1253 좋다
# Baekjoon 1253

# Created by sw0817 on 2021. 03. 12..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1253

N = int(input())
nums = list(map(int, input().split()))

result = 0

# 정렬
nums.sort()

for i in range(N):

    # 현재 값 빼고 중에 두 개를 고르면 됨
    temp = nums[:i] + nums[i+1:]

    # 젤 작은 값 + 젤 큰 값
    start, end = 0, len(temp)-1
    while start < end:

        # 있으면 검사 끝
        num = temp[start] + temp[end]
        if num == nums[i]:
            result += 1
            break

        # 현재 값이 작으면 왼쪽을 늘려주고
        if num < nums[i]:
            start += 1

        # 크면 오른쪽을 줄여주고
        else:
            end -= 1

print(result)
