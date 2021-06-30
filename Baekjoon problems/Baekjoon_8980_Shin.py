# 백준 8980 택배
# Baekjoon 8980

# Created by sw0817 on 2021. 06. 30..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/8980

# 남는 자리를 부분적으로도 적재 가능하기 때문에, 가까운 곳에 배송할 수 있는 만큼 싣는게 중요
N, C = map(int, input().split())
M = int(input())
info = []
for _ in range(M):
    info.append(list(map(int, input().split())))

# 가까운 도착지 순으로 정렬
info.sort(key=lambda x: (x[1], x[0]))
dp = [C] * N
result = 0

for i in range(M):
    temp = C
    for j in range(info[i][0]-1, info[i][1]-1):
        temp = min(temp, dp[j])
    temp = min(temp, info[i][2])
    for j in range(info[i][0]-1, info[i][1]-1):
        dp[j] -= temp
    result += temp

print(result)