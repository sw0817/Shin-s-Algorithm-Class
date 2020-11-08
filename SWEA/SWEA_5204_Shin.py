# SWEA 5204 병합 정렬
# SWEA 5204

# Created by sw0817 on 2020. 11. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def merge(left, right):
    global cnt
    len_left = len(left)
    len_right = len(right)
    result = [0] * (len_left + len_right)

    result_i = left_i = right_i = 0

    if left[-1] > right[-1]:
        cnt += 1

    while left_i != len_left and right_i != len_right:
        if left[left_i] <= right[right_i]:
            result[result_i] += left[left_i]
            left_i += 1
            result_i += 1
        else:
            result[result_i] += right[right_i]
            right_i += 1
            result_i += 1
    if left_i != len_left:
        while left_i != len_left:
            result[result_i] += left[left_i]
            left_i += 1
            result_i += 1

    if right_i != len_right:
        while right_i != len_right:
            result[result_i] += right[right_i]
            right_i += 1
            result_i += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    final = merge_sort(nums)
    target = final[N//2]

    print('#{} {} {}'.format(tc, target, cnt))