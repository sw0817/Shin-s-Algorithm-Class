def solution(s):
    answer = ''
    l = len(s)
    idx = 0
    while idx < l:
        if s[idx] == 'z':
            answer += '0'
            idx += 4
            continue
        elif s[idx] == 'o':
            answer += '1'
            idx += 3
            continue
        elif s[idx] == 't':
            if s[idx + 1] == 'w':
                answer += '2'
                idx += 3
                continue
            else:
                answer += '3'
                idx += 5
                continue
        elif s[idx] == 'f':
            if s[idx + 1] == 'o':
                answer += '4'
            else:
                answer += '5'
            idx += 4
            continue
        elif s[idx] == 's':
            if s[idx + 1] == 'i':
                answer += '6'
                idx += 3
            else:
                answer += '7'
                idx += 5
            continue
        elif s[idx] == 'e':
            answer += '8'
            idx += 5
            continue
        elif s[idx] == 'n':
            answer += '9'
            idx += 4
            continue
        else:
            answer += s[idx]
            idx += 1
            continue

    return int(answer)