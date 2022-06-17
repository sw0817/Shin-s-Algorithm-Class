def solution(arr, divisor):
    answer = []

    for n in arr:
        if not n % divisor:
            answer.append(n)

    return sorted(answer) if answer else [-1]