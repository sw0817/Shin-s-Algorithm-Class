# 백준 1029 그림 교환
# Baekjoon 1029

# Created by sw0817 on 2020. 12. 04..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1029

def sell(price, num, idx):
    global people
    if num > people:
        people = num

    for i in range(N):
        if i != idx and not visited[i] and price <= prices[idx][i]:
            visited[i] = 1
            sell(prices[idx][i], num+1, i)
            visited[i] = 0


N = int(input())

prices = [list(map(int, input())) for _ in range(N)]

people = 1

visited = [0] * N
visited[0] = 1

for i in range(1, N):
    visited[i] = 1
    sell(prices[0][i], 2, i)
    visited[i] = 0

print(people)