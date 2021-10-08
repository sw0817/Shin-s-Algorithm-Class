def solution(answers):
    answer = []
    first = [1, 2, 3, 4 ,5] * 2
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    while len(answers) >= len(second):
        first = first * 2
        second = second * 2
        third = third * 2
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first[i]:
            scores[0] += 1
        if answers[i] == second[i]:
            scores[1] += 1
        if answers[i] == third[i]:
            scores[2] += 1
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i+1)
    return answer