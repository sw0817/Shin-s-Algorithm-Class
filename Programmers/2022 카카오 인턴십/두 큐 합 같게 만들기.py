def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    half = (sum1 + sum2) // 2

    i = 0
    j = 0
    l1 = len(queue1)

    while i < 2 * l1 and j < 2 * l1 and sum1 != sum2:
        if sum1 < sum2:
            sum1 += queue2[j]
            sum2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1

        else:
            sum2 += queue1[i]
            sum1 -= queue1[i]
            queue2.append(queue1[i])
            i += 1

    if sum1 == sum2:
        return i + j

    return -1