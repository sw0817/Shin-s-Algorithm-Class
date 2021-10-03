# 백준 1111 IQ Test
# Baekjoon 1111

# Created by sw0817 on 2020. 12. 31..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1111

def find():
    if N == 1:
        print('A')
        return

    elif N == 2:
        if numbers[0] != numbers[1]:
            print('A')
        else:
            print(numbers[0])
        return

    else:
        if numbers[1] - numbers[0] == 0:
            a = 0
            b = numbers[1]
        else:
            a = (numbers[2]-numbers[1]) // (numbers[1]-numbers[0])
            b = numbers[1] - numbers[0] * a

        check = True
        for i in range(1, N):
            if numbers[i] != numbers[i-1] * a + b:
                check = False
                break

        if check:
            print(numbers[N-1] * a + b)
        else:
            print('B')

N = int(input())
numbers = list(map(int, input().split()))

find()