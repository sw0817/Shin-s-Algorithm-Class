# SWEA 5648 원자 소멸 시뮬레이션
# SWEA 5648

# Created by sw0817 on 2020. 12. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://swexpertacademy.com/main/code/problem/problemSolverCodeDetail.do

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    atoms = []
    directs = [set() for _ in range(4)]
    # 원자들의 x 위치, y 위치, 이동 방향 d, 보유 에너지 K
    # 이동 방향은 상(0), 하(1), 좌(2), 우(3)
    for i in range(N):
        x, y, d, K = map(int, input().split())
        atoms.append((x, y, K))
        directs[d].add(i)

    checklist = []
    # 수직으로 마주보는 경우 (x 일치) 상(0), 하(1), 
    for i in directs[0]:
        x_1, y_1 = atoms[i][0], atoms[i][1]
        for j in directs[1]:
            x_2, y_2 = atoms[j][0], atoms[j][1]
            if x_1 == x_2 and y_1 < y_2:
                checklist.append(((y_2 - y_1) / 2, i, j))

    # 수평으로 마주보는 경우 (y 일치) 좌(2), 우(3)
    for i in directs[2]:
        x_1, y_1 = atoms[i][0], atoms[i][1]
        for j in directs[3]:
            x_2, y_2 = atoms[j][0], atoms[j][1]
            if y_1 == y_2 and x_1 > x_2:
                checklist.append(((x_1 - x_2) / 2, i, j))

    # 교차하는 경우
    for i in directs[0]:
        x_1, y_1 = atoms[i][0], atoms[i][1]
        for j in directs[2]:  # 상(0), 좌(2)
            x_2, y_2 = atoms[j][0], atoms[j][1]
            if x_1 < x_2 and y_1 < y_2 and (x_2 - x_1 == y_2 - y_1):
                checklist.append(((x_2 - x_1), i, j))

        for j in directs[3]:  # 상(0), 우(3)
            x_2, y_2 = atoms[j][0], atoms[j][1]
            if x_1 > x_2 and y_1 < y_2 and (x_1 - x_2 == y_2 - y_1):
                checklist.append((x_1 - x_2, i, j))

    for i in directs[1]:
        x_1, y_1 = atoms[i][0], atoms[i][1]

        for j in directs[2]:  # 상(0), 좌(2)
            x_2, y_2 = atoms[j][0], atoms[j][1]
            if x_1 < x_2 and y_1 > y_2 and (x_2 - x_1 == y_1 - y_2):
                checklist.append((x_2 - x_1, i, j))

        for j in directs[3]:  # 상(0), 우(3)
            x_2, y_2 = atoms[j][0], atoms[j][1]
            if x_1 > x_2 and y_1 > y_2 and (x_1 - x_2 == y_1 - y_2):
                checklist.append((x_1 - x_2, i, j))

    checklist.sort(lambda a: a[0])
    front = 0

    dead = [False] * N
    result = 0
    while front < len(checklist):
        # 같은 시간에 사라지는 원자들 집합
        d_list = set()
        time = checklist[front][0]
        while front < len(checklist) and checklist[front][0] == time:
            atom_1, atom_2 = checklist[front][1], checklist[front][2]
            front += 1
            if dead[atom_1] or dead[atom_2]:
                continue
            d_list.add(atom_1)
            d_list.add(atom_2)

        # 원자 폭발
        for atom_id in d_list:
            result += atoms[atom_id][2]
            dead[atom_id] = True

    print("#{} {}".format(tc, result))