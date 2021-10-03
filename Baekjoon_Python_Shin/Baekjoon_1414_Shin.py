# 백준 1414 불우이웃돕기
# Baekjoon 1414

# Created by sw0817 on 2021. 01. 15..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1414

# 총 랜선 길이를 구하고, 연결되는 랜선 정보를 저장한다.
def make_wires():
    total = 0
    for i in range(N):
        row = input()
        for j in range(N):
            if 97 <= ord(row[j]):
                w = ord(row[j]) - 96
            elif 65 <= ord(row[j]):
                w = ord(row[j]) - 38
            else:
                w = 0

            if w != 0:
                edges.append((w, i, j))
                total += w
    return total


# 크루스칼 알고리즘
def make_roots():
    for i in range(N):
        roots[i] = i
        sizes[i] = 1


def find_root(v):
    while v != roots[v]:
        v = roots[v]
    return roots[v]


def union(v_root, u_root):
    if sizes[v_root] < sizes[u_root]:
        roots[v_root] = u_root
        sizes[u_root] += sizes[v_root]
    else:
        roots[u_root] = v_root
        sizes[v_root] += sizes[u_root]


def kruskal():
    # 최소 신장 트리
    MST = []

    # 각 정점을 만든다.
    make_roots()

    # 간선을 오름차순 정렬한다.
    sorted_edges = sorted(edges, key = lambda edge: edge[0])

    for edge in sorted_edges:
        weight, v, u = edge

        # 루트가 다르면
        v_root = find_root(v)
        u_root = find_root(u)

        if v_root != u_root:
            # 합친다.
            union(v_root, u_root)
            # 그리고 MST에 추가한다.
            MST.append(edge)

        # MST의 크기가 N-1이면 종료
        if len(MST) == N-1:
            break

    # MST가 만들어지지 않았다면
    if len(MST) < N-1:
        return -1
    else:
        return MST


N = int(input())

roots = {}
sizes = {}
edges = []

total = make_wires()
MST = kruskal()

if MST == -1:
    print(MST)
else:
    sum_wires = 0
    for edge in MST:
        sum_wires += edge[0]

    print(total - sum_wires)