# 백준 10830 행렬 제곱
# Baekjoon 10830

# Created by sw0817 on 2022. 05. 10..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10830

def cal(arr1, arr2):
   cur = [[0] * n for _ in range(n)]
   for i in range(n):
      for j in range(n):
         for k in range(n):
            cur[i][j] += arr1[i][k] * arr2[k][j]
         cur[i][j] %= 1000

   return cur


n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * i + [1] + [0] * (n-i-1) for i in range(n)]

while b > 0:
   if b % 2 == 1:
      result = cal(result, arr)
   arr = cal(arr, arr)
   b //= 2

for i in range(n):
   for j in range(n):
      print(int(result[i][j]), end=' ')
   print()