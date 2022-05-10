from functools import cmp_to_key


def compare(a, b):
    l1, l2 = len(a[0]), len(b[0])
    i = 0
    while i < min(l1, l2):
        o1, o2 = ord(a[0][i]), ord(b[0][i])
        if o1 < 97:
            o1 += 32
        if o2 < 97:
            o2 += 32

        if o1 > o2:
            return 1
        elif o1 < o2:
            return -1

        i += 1

    if l2 < l1:
        return 1
    elif l1 < l2:
        return -1

    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1

    if a[2] > b[2]:
        return 1
    elif a[2] == b[2]:
        return 0
    else:
        return -1


def solution(files):
    answer = []

    new_files = []
    for j in range(len(files)):
        file = files[j]
        cur = []
        idx = 0
        l = len(file)
        while idx < l:
            try:
                i = int(file[idx])
                break
            except:
                idx += 1
        cur.append(file[:idx])
        n = ""
        idx2 = idx
        while idx2 < l and idx2 < idx + 5:
            try:
                n += str(int(file[idx2]))
                idx2 += 1
            except:
                break
        cur.append(int(n))
        cur.append(j)
        new_files.append(cur)

    new_files = sorted(new_files, key=cmp_to_key(compare))

    for file in new_files:
        answer.append(files[file[2]])

    return answer