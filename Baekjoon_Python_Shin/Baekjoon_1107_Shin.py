# 백준 1107 리모콘
# Baekjoon 1107

# Created by sw0817 on 2021. 03. 08..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1107

N = int(input())
M = int(input())

# M == 0 이면 input 이 하나 없다.
if M:
    mal = list(map(str, input().split()))

# in 을 쓰기 위해 str 집합 set 로 설정.
num = set([str(i) for i in range(10)])
for i in range(M):
    num.remove(mal[i])

# 현재 채널 100에서 위 아래 키로 가는 방법.
min_cnt = abs(N-100)

# 채널은 무한하지만 N <= 500000 에 도달하기 위해 499900 번 이상 움직이는건 손해.
for i in range(999895):

    # 현재 가능 키로 i채널 도달 가능 여부
    able = True
    for j in str(i):
        if j not in num:
            able = False
            break

    # 가능하면 버튼 클릭 횟수 비교한다.
    if able:
        min_cnt = min(min_cnt, abs(N-i)+len(str(i)))

print(min_cnt)