from bisect import bisect_left

def solution(info, query):
    answer = []

    # 모든 정보에 대한 배열을 만든다.
    # 언어(-, cpp, java, python) * 직군(-, backend, frontend)
    # * 경력(-, junior, senior) * 소울푸드(-, chicken, pizza)
    # 4 * 3 * 3 * 3 = 108
    # n * (3 * 3 * 3) + m * (3 * 3) + k * (3) + l
    info_list = [[] for _ in range(108)]
    # 문자열을 index로 변환해서 사용할 수 있게 매핑
    case_map = {
        '-':0, 'cpp':1, 'java':2, 'python':3,
        'backend':1, 'frontend':2,
        'junior':1, 'senior':2,
        'chicken':1, 'pizza':2
    }

    for case in info:
        case = case.split()
        arr = (case_map[case[0]]*3*3*3,
               case_map[case[1]]*3*3,
               case_map[case[2]]*3,
               case_map[case[3]]
               )
        score = int(case[4])

        for i in range(1 << 4):
            idx = 0
            for j in range(4):
                if i & (1 << j):
                    idx += arr[j]

            info_list[idx].append(score)

    for i in range(108):
        info_list[i] = sorted(info_list[i])

    for string in query:
        case = string.split()
        idx = case_map[case[0]]*3*3*3 + case_map[case[2]]*3*3 + case_map[case[4]]*3 + case_map[case[6]]
        score = int(case[7])
        answer.append(len(info_list[idx]) - bisect_left(info_list[idx], score))

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))