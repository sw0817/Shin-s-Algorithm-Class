from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def findTableBlock(table, l):
    visited = [[0] * l for _ in range(l)]
    blocks = []
    for i in range(l):
        for j in range(l):
            if not visited[i][j] and table[i][j]:
                queue = deque()
                block = []
                min_r = l
                min_c = l
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    r, c = queue.popleft()
                    min_r = min(min_r, r)
                    min_c = min(min_c, c)
                    block.append([r, c])
                    for dr, dc in move:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < l and 0 <= nc < l and not visited[nr][nc] and table[nr][nc]:
                            visited[nr][nc] = 1
                            queue.append((nr, nc))

                for loc in block:
                    loc[0] -= min_r
                    loc[1] -= min_c

                blocks.append(block)

    return blocks


def findBoardBlock(board, l):
    visited = [[0] * l for _ in range(l)]
    blocks = []
    for i in range(l):
        for j in range(l):
            if not visited[i][j] and not board[i][j]:
                queue = deque()
                block = []
                min_r = l
                min_c = l
                max_r = 0
                max_c = 0
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    r, c = queue.popleft()
                    min_r = min(min_r, r)
                    min_c = min(min_c, c)
                    max_r = max(max_r, r)
                    max_c = max(max_c, c)
                    block.append([r, c])
                    for dr, dc in move:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < l and 0 <= nc < l and not visited[nr][nc] and not board[nr][nc]:
                            visited[nr][nc] = 1
                            queue.append((nr, nc))

                for loc in block:
                    loc[0] -= min_r
                    loc[1] -= min_c

                max_r -= min_r
                max_c -= min_c

                blocks.append([block, max_r, max_c])

    return blocks


def rotation(block, max_r, max_c):
    ret = [block]

    for _ in range(3):
        nxt = []

        for loc in ret[-1]:
            nxt.append([loc[1], max_r-loc[0]])
        ret.append(sorted(nxt))
        max_r, max_c = max_c, max_r

    return ret


def solution(game_board, table):

    answer = 0

    l = len(game_board)
    blocks = findBoardBlock(game_board, l)
    rotation_blocks = []
    for block, max_r, max_c in blocks:
        block.sort()
        rotation_blocks.append(rotation(block, max_r, max_c))

    l_r = len(rotation_blocks)
    visited = [0] * l_r

    tableBlocks = findTableBlock(table, l)

    for tB in tableBlocks:
        tB.sort()
        for i in range(l_r):
            if tB in rotation_blocks[i] and not visited[i]:
                visited[i] = 1
                answer += len(tB)
                break

    return answer


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board, table))