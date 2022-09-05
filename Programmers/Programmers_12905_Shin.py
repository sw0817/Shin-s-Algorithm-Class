def solution(board):
    r = len(board)
    c = len(board[0])
    l = board[0][0]

    for i in range(1, r):
        for j in range(1, c):
            if board[i][j]:
                board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
            l = max(l, board[i][j])

    return l ** 2