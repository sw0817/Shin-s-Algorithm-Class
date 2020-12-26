# 백준 1043 저울
# Baekjoon 1043

# Created by sw0817 on 2020. 12. 26..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1043

# 사람의 수 N, 파티의 수 M
N, M = map(int, input().split())

# 진실을 아는 사람 수와 번호
fact = list(map(int, input().split()))

# 진실을 아는 사람 수
F = fact[0]

# 그 번호
F_nums = fact[1:]

# 사람들이 진실을 아는지 여부
members = [0] * N
for i in range(F):
    members[F_nums[i]-1] = 1

# 각 파티에 참여하는 사람 정보
parties = []

# 각 파티에서 진실을 말해야하는지 여부
truth_talks = [0] * M

for _ in range(M):
    guests = list(map(int, input().split()))[1:]
    parties.append(guests)

# 각 파티에서 진실을 아는자가 있는지
for i in range(M):
    continues = 0
    for member in parties[i]:

        # 있다면
        if members[member-1]:
            continues = 1

            # 진실을 말한다.
            truth_talks[i] = 1
            break

    # 진실을 말했다면
    if continues:
        for member in parties[i]:

            # 진실을 아는자 갱신
            members[member-1] = 1

# 새롭게 진실을 아는자가 생겼다면 다시 첫 파티부터 확인
re = 1
while re:
    re = 0
    for i in range(M):
        if truth_talks[i]:
            continue

        else:
            continues = 0
            for member in parties[i]:
                if members[member-1]:
                    continues = 1
                    truth_talks[i] = 1
                    break

            if continues:
                re = 1
                for member in parties[i]:
                    members[member-1] = 1

print(M - sum(truth_talks))


