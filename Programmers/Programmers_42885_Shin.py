def solution(people, limit):
    answer = 0

    people.sort()
    l = len(people)

    i = 0
    j = l - 1

    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return answer