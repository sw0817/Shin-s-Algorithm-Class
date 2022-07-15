def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a = 0
    l = len(A)
    for b in B:
        if A[a] < b:
            answer += 1
            a += 1
    return answer