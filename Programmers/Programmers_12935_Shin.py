def solution(arr):
    answer = []
    m = min(arr)
    for n in arr:
        if not n == m:
            answer.append(n)
    return answer if answer else [-1]