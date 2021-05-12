# 백준 2407 조합
# Baekjoon 2407

# Created by sw0817 on 2021. 05. 13..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2407

import math

n, m = map(int, input().split())
print(math.factorial(n) // ((math.factorial(n - m)) * (math.factorial(m))))
