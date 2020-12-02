# 백준 2839 설탕 배달
# Baekjoon 2839

# Created by sw0817 on 2020. 12. 02..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2839

N = int(input())

# 사용하는 봉지 수
result = 0

# 5kg 봉지 최대한 많이 쓰는게 좋음
m = N // 5

# 5kg 봉지로 모두 처리가 가능하면
if N - (m * 5) == 0:
    result = m

# 안된다면 5kg 봉지를 하나씩 줄이며 검사
else:
    while m >= 0:
        # 5kg 봉지로 최대한 처리하고, 나머지 3kg 봉지일 때 남는 양
        temp = (N - (m * 5)) % 3

        # 남는 양이 없으면
        if temp == 0:

            # 그것이 최고의 효율이다.
            result = (N - (m * 5)) // 3 + m
            break

        # 처리 안되면 5kg 봉지를 줄인다.
        else:
            m -= 1

# 5kg 봉지를 사용하지 않아도 처리가 안된다면
if result == 0:

    # 불가능
    print(-1)

else:
    print(result)