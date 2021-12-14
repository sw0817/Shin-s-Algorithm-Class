# 백준 7579 앱
# Baekjoon 7579

# Created by sw0817 on 2021. 12. 14..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/7579

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
# 최대 사용 비용
max_cost = sum(costs)
# i 만큼의 비용 사용했을 때 최대 확보 메모리 배열
dp = [0] * (max_cost + 1)

# i 번째 앱을 비활성화 시
for i in range(N):
    # 현재 j비용 사용 시 최대 확보 메모리와 i 번째 앱 비용을 사용해 j비용이 사용 된 경우를 비교
    for j in range(max_cost, costs[i]-1, -1):
        dp[j] = max(dp[j], dp[j-costs[i]] + memories[i])

# 최저로 사용한 비용으로 M 이상의 메모리 확보한 비용을 찾는다.
for i in range(max_cost+1):
    if M <= dp[i]:
        print(i)
        break