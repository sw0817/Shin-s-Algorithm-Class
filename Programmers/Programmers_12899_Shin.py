def solution(n):
    answer = ''

    nums = ['1', '2', '4']
    while n:
        answer += nums[(n-1) % 3]
        if n % 3:
            n //= 3
        else:
            n = n // 3 - 1

    return "".join(reversed(answer))