def solution(s):
    cnt = 0
    for a in s:
        if a == 'p' or a == 'P':
            cnt += 1
        elif a == 'y' or a == 'Y':
            cnt -= 1

    answer = True if cnt == 0 else False
    return answer