# SWEA 4050 재관이의 대량 할인
# SWEA 4050

# Created by sw0817 on 2021. 03. 11..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIseXoKEUcDFAWN

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    price.sort()
    ans = sum(price)
    for i in range(n-3, -1, -3):
        ans -= price[i]
    print('#'+str(test_case), ans)