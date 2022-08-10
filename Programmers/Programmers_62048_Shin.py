from math import gcd

def solution(w,h):
    return w * h + gcd(w, h) - (w + h)