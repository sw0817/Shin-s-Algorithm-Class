Board = []
cur = set()
M = N = 0
checkPos = [(1, 0), (0, 1), (1, 1)]


def blockDown():
    for j in range(N):
        low = 0
        for i in range(M - 1, -1, -1):
            if Board[i][j] == 0:
                low = max(i, low)
            elif low:
                Board[i][j], Board[low][j] = 0, Board[i][j]
                low -= 1


def checkBlock(r, c, b):
    for dr, dc in checkPos:
        nr, nc = r + dr, c + dc
        if Board[nr][nc] != b:
            return False
    cur.add((r, c))
    for dr, dc in checkPos:
        nr, nc = r + dr, c + dc
        cur.add((nr, nc))
    return True


def solution(m, n, board):
    global Board, cur, M, N

    for i in range(m):
        board[i] = list(board[i])

    Board, M, N = board, m, n
    answer = 0

    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if Board[i][j]:
                    checkBlock(i, j, Board[i][j])
        if not cur:
            break

        answer += len(cur)
        for r, c in cur:
            Board[r][c] = 0

        cur = set()
        blockDown()

    return answer