def solution(brown, yellow):
    answer = []
    w = brown + yellow
    for i in range(w, 2, -1):
        if not w % i:
            r = w // i
            if yellow == (i-2) * (r-2):
                return [i, r]