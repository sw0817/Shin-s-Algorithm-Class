def solution(lottos, win_nums):
    answer = []

    win = 0
    zero = 0

    for num in lottos:
        if not num:
            zero += 1
        elif num in win_nums:
            win += 1

    top = 7 - (win + zero)
    if top == 7:
        top -= 1

    answer.append(top)

    bottom = 7 - win
    if bottom == 7:
        bottom -= 1

    answer.append(bottom)

    return answer