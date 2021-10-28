def solution(name):
    answer = 0
    l = len(name)
    left, right = l, 0

    # 왼쪽으로 쓸든 오른쪽으로 쓸든 두 가지 방법 뿐
    # 우선 전체 알파벳의 위치에서 입력 횟수를 구함
    inputCnt = [0] * l
    for i in range(l):
        inputCnt[i] = min(abs(ord(name[i]) - 65), 90 - ord(name[i]) + 1)
        if inputCnt[i]:
            right = i

    for i in range(l - 1, 0, -1):
        if inputCnt[i]:
            left = i

    basic = sum(inputCnt)
    answer = min(right, l - left) + basic

    return answer