def solution(n):
    answer = ''

    while n:
        n, mod = divmod(n, 3)
        answer += str(mod)

    answer = int(answer[::-1])

    while not answer % 10:
        answer //= 10

    answer = str(answer)

    ret = 0

    for i in range(len(answer)):
        ret += 3 ** i * int(answer[i])

    return ret