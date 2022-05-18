def toMs(h, m, s, ms):
    ret = h * 3600000 + m * 60000 + s * 1000 + ms
    return ret


def calTime(s):
    ret = int(float(s[:-1]) * 1000)
    return ret


def solution(lines):
    answer = 0
    l = len(lines)
    arr = []
    for line in lines:
        d, t, T = map(str, line.split())
        e = toMs(int(t[:2]), int(t[3:5]), int(t[6:8]), int(t[9:]))
        arr.append([e - calTime(T) + 1, e])

    arr.sort(key=lambda x: x[1])

    for i in range(l):
        temp = 1
        start, end = arr[i]
        for j in range(i+1, l):
            if arr[j][0] <= end + 999:
                temp += 1
            else:
                continue

        answer = max(answer, temp)

    return answer