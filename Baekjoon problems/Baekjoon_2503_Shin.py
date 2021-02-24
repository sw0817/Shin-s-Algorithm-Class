# 백준 2503 숫자야구
# Baekjoon 2503

# Created by sw0817 on 2021. 02. 24..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2503

# 질문, 결과(스트라이크, 볼)
def check(q, s, b):

    # 인덱스로 비교(스트라이크), 포함 체크(볼) 하기 위해 문자열화하여 배열에 저장
    question = list(str(q))

    # 가능한 모든 경우의 수 중
    for num in range(123, 1000):

        # 아직 가능한 경우
        if pos[num]:
            strike = 0
            ball = 0

            # 스트라이크와 볼 개수 체크
            n = str(num)
            for i in range(3):
                if n[i] == question[i]:
                    strike += 1
                elif n[i] in question:
                    ball += 1

            # 조건과 다르면 불가능한 경우
            if s != strike or b != ball:
                pos[num] = False


N = int(input())

# 문제는 123 ~ 987까지 가능한데 for문 편하게 999까지
pos = [False] * 1000
for i in range(10):
    for j in range(10):
        for k in range(10):
            # 0은 포함되면 안 되고, i, j, k가 모두 달라야 함
            if i and j and k and i != j and i != k and j != k:
                pos[100*i+10*j+k] = True

for _ in range(N):

    # 질문으로 가능한 경우 체크
    q, s, b = map(int, input().split())
    check(q, s, b)

# 가능 경우 수
result = 0

# 문제는 123 ~ 987까지 가능
for i in range(123, 988):
    if pos[i]:
        result += 1

print(result)