# 백준 16196 중국 신분증 번호
# Baekjoon 16196

# Created by sw0817 on 2022. 10. 12..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/16196

big = ['01', '03', '05', '07', '08', '10', '12']
mid = ['04', '06', '09', '11']

def dayValid(year, month, day):

    if not '1900' <= year <= '2011' or not '01' <= month <= '12':
        return False

    if month in big:
        if not '01' <= day <= '31':
            return False
    elif month in mid:
        if not '01' <= day <= '30':
            return False
    elif month == '02':
        max_day = '28'
        if not int(year) % 4 and int(year) % 100 or not int(year) % 400:
            max_day = '29'

        if not '01' <= day <= max_day:
            return False
    else:
        return False
    return True


code = input()
N = int(input())
valid = False
for _ in range(N):
    lo_code = input()
    if code[:6] == lo_code:
        valid = True

if not dayValid(code[6:10], code[10:12], code[12:14]):
    valid = False

x = 0
if code[17] == 'X':
    x += 10
else:
    x += int(code[17])
for i in range(17):
    x += 2 ** (17 - i) * int(code[i])

if code[14:17] == '000':
    valid = False

if not x % 11 == 1:
    valid = False

if not valid:
    print('I')
elif int(code[14:17]) % 2:
    print('M')
else:
    print('F')