# 백준 1545 안티 팰린드롬
# Baekjoon 1545

# Created by sw0817 on 2021. 08. 27..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1545

def solution():
    text = input()
    text = sorted(text)
    l = len(text)
    result = []
    for i in range(l):
        for j in range(len(text)):
            if i * 2 < l or text[j] != result[l-1-i]:
                result.append(text.pop(j))
                break
        else:
            return -1

    return "".join(result)


print(solution())