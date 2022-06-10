def solution(relation):
    answer = []
    r, c = len(relation), len(relation[0])

    for j in range(1, 1 << c):
        for bit in answer:
            if bit & j == bit:
                break
        else:
            temp_set = set()
            for rel in relation:
                temp = []
                for i in range(c):
                    if j & (1 << i):
                        temp.append(rel[i])
                temp_set.add(tuple(temp))
            if len(temp_set) == r:
                answer.append(j)

    return len(answer)