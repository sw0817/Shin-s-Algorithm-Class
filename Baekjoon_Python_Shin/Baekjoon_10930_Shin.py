# 백준 10930 SHA-256
# Baekjoon 10930

# Created by sw0817 on 2022. 09. 25..
# Copyright © 2022 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/10930

from hashlib import sha256
print(sha256(input().encode()).hexdigest())