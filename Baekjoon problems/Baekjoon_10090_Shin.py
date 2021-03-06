# 백준 10090 Counting Inversions
# Baekjoon 10090

# Created by sw0817 on 2021. 03. 06..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10090

# 머지소트를 활용한다.
# 반으로 나눈 뒤 합치는 과정에서 오른쪽 배열에서 왼쪽으로 수가 들어갈 때,
# 왼쪽 배열에 남아있는 수의 수가 바꿔주어야 하는 쌍의 수

def merge(x, y):
    global result
    lx, ly = len(x), len(y)
    i, j = 0, 0
    temp = []
    while i < lx and j < ly:
        if x[i] > y[j]:
            temp.append(y[j])
            j += 1
            result += lx - i
        else:
            temp.append(x[i])
            i += 1

    if i == lx:
        temp.extend(y[j:])
    else:
        temp.extend(x[i:])

    return temp


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = 0
    right = len(arr)-1
    mid = (left+right) // 2
    return merge(merge_sort(arr[left:mid+1]), merge_sort(arr[mid+1:]))


N = int(input())
permutations = list(map(int, input().split()))
result = 0
merge_sort(permutations)

print(result)