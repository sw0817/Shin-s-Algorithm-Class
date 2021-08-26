# 백준 1036 36진수
# Baekjoon 1036

# Created by sw0817 on 2021. 08. 26..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1036

N = int(input())
# 0~9, A~Z
arr = [0 for _ in range(36)]
result = 0
for _ in range(N):
    text = input()
    for i in range(len(text) - 1, -1, -1):
        alph = text[i]
        try:
            if 0 <= int(alph) <= 9:
                arr[int(alph)] += (36 ** (len(text) - i - 1)) * (35 - int(alph))
                result += (36 ** (len(text) - i - 1)) * int(alph)
        except:
            arr[ord(alph) - 55] += (36 ** (len(text) - i - 1)) * (35 - (ord(alph) - 55))
            result += 36 ** (len(text) - i - 1) * (ord(alph) - 55)
K = int(input())

arr = sorted(arr, reverse=True)
for i in range(K):
    result += arr[i]

if not result:
    print(0)

result_text = ""

while result:
    cur = result % 36
    if 0 <= cur < 10:
        result_text = str(cur) + result_text
    else:
        result_text = chr(cur+55) + result_text
    result //= 36

print(result_text)