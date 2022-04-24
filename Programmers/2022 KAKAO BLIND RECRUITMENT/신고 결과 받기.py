def solution(id_list, report, k):
    l = len(id_list)
    answer = [0] * l
    report_list = [set() for _ in range(l)]

    for rp in report:
        s, e = map(str, rp.split())
        report_list[id_list.index(e)].add(s)

    for i in range(l):
        if k <= len(report_list[i]):
            for id in report_list[i]:
                answer[id_list.index(id)] += 1

    return answer