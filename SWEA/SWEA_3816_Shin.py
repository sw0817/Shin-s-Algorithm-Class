# SWEA 3816 [Professional] 아나그램
# SWEA 3816

# Created by sw0817 on 2021. 04. 12..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())
for tc in range(1, T+1):
    s1, s2 = input().split()
    l1, l2 = len(s1), len(s2)
    result = 0
    anaSet = set()
    basic = [0] * 26
    for i in range(l1):
        basic[ord(s1[i]) - 97] += 1

    temp = [0] * 26
    for i in range(l1):
        temp[ord(s2[i]) - 97] += 1
    if basic == temp:
        result += 1

    for i in range(l2-l1):
        temp[ord(s2[i]) - 97] -= 1
        temp[ord(s2[i+l1]) - 97] += 1
        if basic == temp:
            result += 1

    print("#{} {}".format(tc, result))