def solution(participant, completion):
    people = dict()
    people_set = set()

    for p in participant:
        if p in people:
            people[p] += 1
        else:
            people[p] = 1
            people_set.add(p)

    for c in completion:
        people[c] -= 1
        if not people[c]:
            people_set.discard(c)

    return list(people_set)[0]