def makeCourse(order, cur, idx, l):
    if idx == l:
        length = len(cur)
        cur = ''.join(sorted(cur))
        try:
            foodMaps[length][cur] += 1
        except:
            foodMaps[length][cur] = 1
        max_cnts[length] = max(max_cnts[length], foodMaps[length][cur])
        return

    makeCourse(order, cur + order[idx], idx + 1, l)
    makeCourse(order, cur, idx + 1, l)


def solution(orders, course):
    answer = []

    for order in orders:
        makeCourse(order, "", 0, len(order))

    for c in course:
        cur_cnt = max_cnts[c]
        if cur_cnt < 2:
            continue
        for order in foodMaps[c]:
            if foodMaps[c][order] == cur_cnt:
                answer.append(order)

    answer.sort()

    return answer


foodMaps = [dict() for _ in range(11)]
max_cnts = [0] * 11