def solution(s, n):
    answer = ''

    for w in s:
        if w == ' ':
            answer += w
        elif 97 <= ord(w) <= 122:
            a = ord(w) + n
            if 122 < a:
                a -= 26
            answer += chr(a)
        else:
            a = ord(w) + n
            if 90 < a:
                a -= 26
            answer += chr(a)

    return answer