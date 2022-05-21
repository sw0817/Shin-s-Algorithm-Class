def solution(board, moves):
    answer = 0

    l = len(board)
    idxs = [l] * l
    for j in range(l):
        for i in range(l):
            if board[i][j]:
                idxs[j] = i
                break

    stack = []
    for m in moves:
        if idxs[m - 1] == l:
            continue
        c = board[idxs[m - 1]][m - 1]
        if stack and stack[-1] == c:
            stack.pop()
            answer += 2
        else:
            stack.append(c)
        idxs[m - 1] += 1

    return answer