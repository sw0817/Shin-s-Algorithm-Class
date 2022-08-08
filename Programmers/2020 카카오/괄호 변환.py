def isBalanced(s):
    p = 0
    for c in s:
        if c == '(':
            p += 1
        else:
            p -= 1
    if p == 0:
        return True


def isRight(s):
    p = 0
    for c in s:
        if c == '(':
            p += 1
        else:
            p -= 1
        if p < 0:
            return

    if p == 0:
        return True


def solution(p):
    answer = ''

    # 1
    if not p or isRight(p):
        return p

    u = ''
    v = ''

    # u,v 나누기
    for i in range(2, len(p) + 1, 2):
        if isBalanced(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    if isRight(u):
        answer += u + solution(v)

    else:
        answer += '(' + solution(v) + ')'
        for c in u[1:-1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('

    return answer