def change(log):
    h, m, s = log.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def reChange(time):
    ret = ""
    hour = time // 3600
    minute = (time - (hour * 3600)) // 60
    sec = time - (hour * 3600) - (minute * 60)
    if 10 <= hour:
        ret += str(hour)
    elif hour:
        ret += "0" + str(hour)
    else:
        ret += "00"
    ret += ":"
    if 10 <= minute:
        ret += str(minute)
    elif minute:
        ret += "0" + str(minute)
    else:
        ret += "00"
    ret += ":"
    if 10 <= sec:
        ret += str(sec)
    elif sec:
        ret += "0" + str(sec)
    else:
        ret += "00"
    return ret


def solution(play_time, adv_time, logs):
    play_time_sec = change(play_time)
    whole_log = [0] * play_time_sec
    for log in logs:
        start, end = log.split('-')
        start, end = change(start), change(end)
        whole_log[start] += 1
        if end < play_time_sec:
            whole_log[end] -= 1

    for i in range(1, play_time_sec):
        whole_log[i] += whole_log[i-1]

    adv_time_sec = change(adv_time)
    idx = 0
    end_idx = adv_time_sec
    maxIdx = 0
    cur = sum(whole_log[idx:idx + adv_time_sec])
    max_sum = cur
    while idx + adv_time_sec < play_time_sec:
        cur += whole_log[end_idx]-whole_log[idx]
        idx += 1
        end_idx += 1
        if max_sum < cur:
            maxIdx = idx
            max_sum = cur

    return reChange(maxIdx)


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))

# new_logs = sorted([change(log) for log in logs])