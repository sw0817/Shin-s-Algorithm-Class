# 백준 1748 제곱ㄴㄴ
# Baekjoon 1748

# Created by sw0817 on 2020. 12. 16..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1748


# 주어진 수
N = input()

# 주어진 수의 자릿수
L = len(N)

# 결과값 초기화
result = 0

# 1의 자리수라면 갯수만큼 더한다.
if L == 1:
    result = int(N)

else:
    # 10의 제곱수 x는 아래와 같은 규칙을 따른다.
    # 자신보다 자릿수가 하나 작은 수를 0.9x 개 가진다.
    # 그 수들의 자릿수는 i-1
    for i in range(L, 1, -1):
        result += (10 ** (i-2)) * 9 * (i-1)

    # 최대 자릿수 숫자의 개수
    rest = int(N) - 10 ** (L-1)
    result += (rest+1) * L

print(result)


# for i in range(1, int(N)+1):
#     result += len(str(i))
#
# print(result)