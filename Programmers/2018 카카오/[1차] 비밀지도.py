def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        cur = [' '] * n
        cur1 = format(arr1[i], '#b')
        cur2 = format(arr2[i], '#b')
        l1 = len(cur1) - 2
        l2 = len(cur2) - 2
        cur1 = '0' * (n - l1) + cur1[2:]
        cur2 = '0' * (n - l2) + cur2[2:]
        for j in range(n):
            if cur1[j] == '1' or cur2[j] == '1':
                cur[j] = '#'

        answer.append("".join(cur))

    return answer