nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def solution(dartResult):
    answer = 0

    l = len(dartResult)
    idx = 0

    last = 0
    cur = 0
    while idx < l:
        if dartResult[idx] in nums:
            cur = 0
            if dartResult[idx + 1] == '0':
                cur += 10
                idx += 1
            else:
                cur += int(dartResult[idx])
        elif dartResult[idx] in ['S', 'D', 'T']:
            if dartResult[idx] == 'D':
                cur *= cur
            elif dartResult[idx] == 'T':
                cur *= cur ** 2
            if idx == l - 1 or dartResult[idx + 1] in nums:
                answer += cur
                last = cur
        else:
            if dartResult[idx] == '*':
                answer += last
                cur *= 2
            else:
                cur *= -1
            answer += cur
            last = cur

        idx += 1

    return answer