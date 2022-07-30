def solution(n):
    m = int(n ** 0.5)
    return (m + 1) ** 2 if m ** 2 == n else -1