from copy import deepcopy

adj = [[] for _ in range(17)]
max_cnt = 0
Info = []

# 갈 수 있는 곳, 양, 늑대
def recur(s, sheep, wolf):
    global adj, max_cnt, Info

    # 더 이상 남은 갈 곳이 없거나 양 다 먹히면
    if sheep == wolf or not s:
        # 갱신
        max_cnt = max(max_cnt, sheep)
        return

    # 갈 수 있는 모든 노드에 대해
    for i in s:
        # 노드 리스트 카피해서
        cur = deepcopy(s)
        # 가는 노드 지우고
        cur.remove(i)
        # 해당 노드 아래 노드 저장해서
        for j in adj[i]:
            cur.append(j)
        # 해당 노드가 늑대
        if Info[i]:
            recur(cur, sheep, wolf + 1)
        # 양
        else:
            recur(cur, sheep + 1, wolf)


def solution(info, edges):
    global adj, Info, max_cnt

    Info = info
    for edge in edges:
        # 자식 노드 번호 저장
        adj[edge[0]].append(edge[1])

    # nodes = 현재 탐색할 수 있는(탐색한 적 없는) 노드 리스트
    nodes = deepcopy(adj[0])
    # 현재는 양 1마리
    recur(nodes, 1, 0)

    return max_cnt