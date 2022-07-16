def solution(x, n):
    return [0] * n if not x else [i for i in range(x, x * (n + 1), x)]