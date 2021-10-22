def solution(arr):
    answer = []

    cur = 10
    for n in arr:
        if not n == cur:
            cur = n
            answer.append(n)

    return answer