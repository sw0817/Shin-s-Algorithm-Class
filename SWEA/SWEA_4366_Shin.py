# SWEA 4366 정식이의 은행업무
# SWEA 4366

# Created by sw0817 on 2020. 11. 01..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd&categoryId=AWMeRLz6kC0DFAXd&categoryType=CODE


def check():
    for i in range(len(binary)):
        temp = binary[i]
        binary[i] = (temp + 1) % 2

        for j in range(len(triple)):
            temp3 = triple[j]
            for k in range(1, 3):
                triple[j] = (temp3 + k) % 3
                bin_num = 0
                tri_num = 0
                for l in range(len(binary)):
                    if binary[l] == 1:
                        bin_num += 2 ** (len(binary)-1 - l)
                for l in range(len(triple)):
                    if triple[l] > 0:
                        tri_num += triple[l] * (3 ** (len(triple)-1 - l))

                if bin_num == tri_num:
                    print('#{} {}'.format(tc, bin_num))
                    return
            triple[j] = temp3
        binary[i] = temp


T = int(input())
for tc in range(1, T+1):
    binary = list(map(int, input()))
    triple = list(map(int, input()))
    check()