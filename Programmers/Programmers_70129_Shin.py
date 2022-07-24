def solution(s):
    answer = [0, 0]

    while s != '1':
        answer[0] += 1
        l = len(s)
        z = s.count('0')
        answer[1] += z
        l -= z
        s = ''
        while l:
            s += str(l % 2)
            l //= 2

    return answer