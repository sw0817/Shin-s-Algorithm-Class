import math

def solution(n, k):
    p = [i for i in range(1, n+1)]
    ret = []
    k = k-1

    while p:
        a = k // math.factorial(n-1)
        ret.append(p[a])
        del p[a]

        k = k % math.factorial(n-1)
        n -= 1

    return ret