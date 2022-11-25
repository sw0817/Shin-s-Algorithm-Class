from itertools import permutations
from copy import deepcopy


def solution(expression):
    answer = 0
    exp = []
    l = len(expression)
    idx = 0
    operation = ["+", "-", "*"]

    cur = ""
    while idx < l:
        if expression[idx] in operation and cur:
            if cur[0] == "-":
                cur = -1 * int(cur[1:])
            else:
                cur = int(cur)
            exp.append(cur)
            exp.append(expression[idx])
            cur = ""
        else:
            cur += expression[idx]
        idx += 1

    if cur:
        if cur[0] == "-":
            cur = -1 * int(cur[1:])
        else:
            cur = int(cur)
        exp.append(cur)

    print(exp)

    for perm in permutations(operation):
        cur_exp = deepcopy(exp)
        l = len(cur_exp)
        idx = 0
        cnt = 0
        cur = 0
        for op in perm:


    return answer


expression = "100-200*300-500+20"
print(solution(expression))