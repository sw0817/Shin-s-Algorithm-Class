# 백준 1214 쿨한 물건 구매
# Baekjoon 1214

# Created by sw0817 on 2021. 03. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1214

# D원 물건 P, Q원 화폐
D, P, Q = map(int, input().split())

# P를 더 큰 수로
if P < Q:
    P, Q = Q, P

# 이 돈 주고는 절대 안 삼
result = D + P + Q

# 한가지 화폐로 딱 맞아 떨어지게 살 수 있으면 그 가격으로
if D % P == 0 or D % Q == 0:
    result = D

else:
    # 이전 가격
    pre_answer = 0

    # 큰 화폐 P를 사용하는 갯수 i
    for i in range(D // P + 1):

        # 나머지 R
        R = D - P * i

        # 나머지를 Q화폐로 딱 나누어 떨어지지 않으면
        if R % Q:
            cur = D - (R % Q) + Q

        # 나누어 떨어지면 최적 방법임. break
        else:
            result = D
            break

        # 현재 가격이 지금까지 최적 방법이면 갱신
        if cur < result:
            result = cur

        # 이전 가격 나왔으면 이제 루프임. break
        if cur == pre_answer:
            break

        # 이전 가격 갱신
        pre_answer = cur

    # P로만 본 가격 조금 넘겨 사는거 체크 안 했으니 마지막 체크
    if P * (D // P + 1) < result:
        result = P * (D // P + 1)

print(result)