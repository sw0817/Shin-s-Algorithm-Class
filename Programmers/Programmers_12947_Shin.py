def solution(x):
    y = 0
    i = 0
    while x // (10 ** i):
        y += (x // (10 ** i)) % 10
        i += 1

    answer = True if not x % y else False

    return answer