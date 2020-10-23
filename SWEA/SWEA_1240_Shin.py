# SWEA 1240 단순 2진 암호코드
# SWEA 1240

# Created by sw0817 on 2020. 10. 23..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    numbers = ['0001101', '0011001','0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    for _ in range(N):
        arr.append(input())
    for row in arr:
        if 0 < int(row):
            for i in range(M-1, -1, -1):
                if row[i] == '1':
                    text = row[i-55:i+1]
                    break
            break
    codes = []
    for i in range(8):
        code = text[i*7:i*7+7]
        codes.append(numbers.index(code))

    check = 0
    for i in range(8):
        if i % 2 == 0:
            check += 3*codes[i]
        else:
            check += codes[i]

    if check % 10 == 0:
        print('#{} {}'.format(tc, sum(codes)))
    else:
        print('#{} {}'.format(tc, 0))
