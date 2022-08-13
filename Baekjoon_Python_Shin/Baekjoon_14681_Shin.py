# 백준 14681 꼬마 정민
# Baekjoon 14681

# Created by sw0817 on 2022. 08. 13..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/14681

def solution(x, y):
    if x < 0:
        if y < 0:
            return 3
        else:
            return 2
    else:
        if y < 0:
            return 4
        else:
            return 1


print(solution(int(input()), int(input())))