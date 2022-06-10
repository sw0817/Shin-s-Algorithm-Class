def solution(relation):
    answer_set = set()
    r = len(relation)
    c = len(relation[0])

    for j in range(1, 1 << c):
        for bit in answer_set:
            if bit & j == bit:
                break
        else:
            temp_set = set()
            for i in range(r):
                temp = []
                for k in range(c):
                    if j & (1 << k):
                        temp.append(relation[i][k])
                temp_set.add(tuple(temp))
            if len(temp_set) == r:
                answer_set.add(j)

    return len(answer_set)