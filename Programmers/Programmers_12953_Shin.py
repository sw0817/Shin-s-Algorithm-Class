from math import gcd

def solution(arr):
    ans = 1

    for a in arr:
        g = gcd(ans, a)
        ans *= a // g

    return ans