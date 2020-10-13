# SWEA 1248 공통조상
# SWEA 1248

# Created by sw0817 on 2020. 10. 13..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD&categoryId=AV15PTkqAPYCFAYD&categoryType=CODE


def tree_depth(n):                                  # 서브트리 크기 구하기
    global result

    if tree[n][0]:                                  # 왼쪽 자식이 있다 ?
        result += 1
        tree_depth(tree[n][0])                      # 그놈 자식도 세

    if tree[n][1]:                                  # 오른쪽에도 자식이 있다 ?
        result += 1
        tree_depth(tree[n][1])                      # 그놈 자식도 세


T = int(input())
for tc in range(1, T+1):
    V, E, son_1, son_2 = map(int, input().split())  # son 맞습니까 ,,
    Es = list(map(int, input().split()))            # Es 말고 뭐라하면 좋을까
    tree = [([0] * 3) for _ in range(V+1)]          # 자식들과 부모 표시 트리

    for i in range(E):
        s = Es[i*2]                                 # 간선의 start
        e = Es[i*2+1]                               # 간선의 end
        if tree[s][0] == 0:                         # 자식 1 (왼쪽 자식)
            tree[s][0] = e
        else:
            tree[s][1] = e                          # 자식 2 (오른쪽 자식)

        tree[e][2] = s                              # 부모

    roots = []                                      # 타겟 자식 1의 부모들 집

    while tree[son_1][2]:                           # 부모가 없을 때까지
        roots.append(tree[son_1][2])                # 타겟의 부모 추가
        son_1 = tree[son_1][2]                      # 부모를 타겟으로 변경

    while not son_2 in roots:                       # 타겟이 (지금은 자식2) 공통 조상이 아니면
        son_2 = tree[son_2][2]                      # 부모를 타겟으로 변경

    result = 1                                      # 자신만으로도 서브트리 크기는 1 확보
    tree_depth(son_2)                               # 공통 조상의 크기 측정

    print('#{} {} {}'.format(tc, son_2, result))    # 출력
