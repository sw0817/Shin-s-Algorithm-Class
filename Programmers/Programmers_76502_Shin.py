from collections import deque

def solution(s):
    l = len(s)
    answer = l
    o = ['[', '{', '(']
    c = [']', '}', ')']
    s += s
    for i in range(l):
        stack = deque()
        for j in range(i, i+l):
            if s[j] in o:
                stack.append(s[j])
            elif stack and stack[-1] in o and o.index(stack[-1]) == c.index(s[j]):
                stack.pop()
            else:
                stack.append(1)
                break
        if stack:
            answer -= 1

    return answer