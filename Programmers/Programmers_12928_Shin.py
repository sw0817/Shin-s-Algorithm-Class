def solution(n):
    answer = 0

    for i in range(1, int(n ** 0.5 + 1)):
        if not n % i:
            answer += i
            if n // i != i:
                answer += n // i

    return answer