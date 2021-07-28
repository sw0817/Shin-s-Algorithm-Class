# 백준 2247 실질적 약수
# Baekjoon 2247

# Created by sw0817 on 2021. 07. 28..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2247

# 쉽게 풀려버린 정답 코드
n = int(input())
result = 0
for i in range(2, n // 2 + 1):
    op = n // i
    result += op * i - i

print(result % 1000000)


######## 아래는 노력한 흔적
n = int(input())
n_sqrt = int(n ** 0.5)
nums = set()
result = 0
for i in range(2, n_sqrt+1):
    if i in nums:
        continue
    nums.add(i)
    # a = (n // i) * i - i
    op = n // i
    result += op * i - i
    print(result)
    print(nums)
    # for j in range(i+1, op+1):
    #     if j in nums:
    #         continue
    #     nums.add(j)
    #     result += n // j * j - j
    #     print(result)
    #     print(nums)

    b = (n // (n // i)) * (n // i) - (n // i)
    # print(i, a, b)
    # result += a
    if not op == n // i:
        result += b

print(result)
print(nums)
# print(n_sqrt)
# exp = [[] for _ in range(n)]
# exp2 = [0] * n
#
# eexp = [[] for _ in range(n)]
# eexp2 = [0] * n
#
# for i in range(2, n+1):
#     cnt = 0
#     for j in range(2, i):
#         if not i % j:
#             cnt += j
#             exp[i-1].append(j)
#     exp2[i-1] = cnt
#
# for i in range(1, n+1):
#     cnt = 0
#     for j in range(2, i+1):
#         if not i % j:
#             cnt += j
#             eexp[i-1].append(j)
#     eexp2[i-1] = cnt
#
# exp2[0] += 1
#
# print(exp)
# print(exp[:n_sqrt+1])
# print(exp2)
# print(sum(exp2))
#
# print(eexp)
# print(eexp[:n_sqrt+1])
# print(eexp2)
# print(eexp2[:n_sqrt+1])
# print(sum(eexp2) - int(n * (n+1) / 2) + 1)
#
# result3 = 0

# 소수 구하고 반대편 약수 보면서 갯수 찾아서 곱하고 더하면 나올듯?
# 집에서 다시

