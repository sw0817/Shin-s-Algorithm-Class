def solution(s):
    stack = []
    cur = s[0]
    stack.append(cur)

    for a in s[1:]:
        if stack and stack[-1] == a:
            stack.pop(-1)
        else:
            stack.append(a)

    return 0 if stack else 1