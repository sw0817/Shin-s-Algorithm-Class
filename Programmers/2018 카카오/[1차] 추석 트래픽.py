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
        s = toMs(int(t[:2]), int(t[3:5]), int(t[6:8]), int(t[9:]))
        arr.append([s, s + calTime(T) + 999])

    arr.sort(key=lambda x: x[1])
    for row in arr:
        print(row)

    for i in range(l):
        temp = 1
        start, end = arr[i]
        for j in range(i+1, l):
            if arr[j][0] <= end:
                temp += 1
            else:
                continue

        answer = max(answer, temp)

    return answer

lines = ["2016-09-15 20:59:57.421 0.351s",
         "2016-09-15 20:59:58.233 1.181s",
         "2016-09-15 20:59:58.299 0.8s",
         "2016-09-15 20:59:58.688 1.041s",
         "2016-09-15 20:59:59.591 1.412s",
         "2016-09-15 21:00:00.464 1.466s",
         "2016-09-15 21:00:00.741 1.581s",
         "2016-09-15 21:00:00.748 2.31s",
         "2016-09-15 21:00:00.966 0.381s",
         "2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))