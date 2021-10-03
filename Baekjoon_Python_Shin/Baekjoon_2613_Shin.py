# 백준 2613 숫자구슬
# Baekjoon 2613

# Created by sw0817 on 2021. 08. 03..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/2613

N, M = map(int, input().split())
beads = list(map(int, input().split()))

# 1. 정답(최소 최댓값 = mid)이 몇 인지를 구한다.
left = 0
right = 1 + N * 100 # sum 계산이 비효율적이므로 30000 or N * 100 이 더 나을 것 같긴 함.

# 2. mid 를 초과하지 않도록 앞에서부터 구슬을 그룹으로 묶는다.
# 3. mid 가 너무 작으면 M개 이상의 그룹으로 나뉜다. => right
def grouping(mid):
    cntList = []
    idx = 0
    cur = 0
    cnt = 0
    l = 0
    while idx < N:
        if mid < cur + beads[idx]:
            if cnt:
                cntList.append(cnt)
                l += 1
                if M < l:
                    return False
                cnt = 1
                cur = beads[idx]
                if mid < cur:
                    return False
            else:
                return False
        else:
            cur += beads[idx]
            cnt += 1
        idx += 1

    if cnt:
        cntList.append(cnt)
        l += 1

    if l == M:
        return True

    if l < M:
        cntSum = l
        for cnt in cntList:
            if 1 < cnt:
                cntSum += cnt - 1
                if M <= cntSum:
                    return True
    return False

final = 1
if N == 1:
    final = right
while left < right:
    mid = (left + right) // 2
    # print("mid", mid)
    if grouping(mid):
        final = mid
        # print("good", final)
        right = mid
    else:
        left = mid + 1

# 4. mid 가 정해졌으면 그룹화 된 구슬 수를 센다.
def countBead(mid):
    print(mid)
    cntList = []
    idx = 0
    cur = 0
    cnt = 0
    l = 0
    while idx < N:
        if mid < cur + beads[idx]:
            if cnt:
                cntList.append(cnt)
                l += 1
                cnt = 1
                cur = beads[idx]
            else:
                return False
        else:
            cur += beads[idx]
            cnt += 1
        idx += 1

    if cnt:
        cntList.append(cnt)
        l += 1

    # print(cntList)
    # idx = 0
    idx = l
    # 오른쪽부터 쪼개기
    cnt = l
    backList = []
    if l < M:
        # # 왼쪽부터 쪼개기
        # cnt = l
        # idx = l
        # for i in range(l):
        #     if cntList[i] == 1:
        #         print(1, end=' ')
        #     else:
        #         if cnt + cntList[i] - 1 <= M:
        #             cnt += cntList[i] - 1
        #             for _ in range(cntList[i]):
        #                 print(1, end=' ')
        #         else:
        #             if cnt == M:
        #                 idx = i
        #                 break
        #             for _ in range((cnt + cntList[i] - 1) - M):
        #                 print(1, end=' ')
        #             print(M + 1 - cnt, end=' ')
        #             idx = i + 1
        #             break

        for i in range(l-1, -1, -1):
            if cntList[i] == 1:
                backList.insert(0, 1)
            else:
                if cnt + cntList[i] - 1 <= M:
                    backList = [1] * cntList[i] + backList
                    cnt += cntList[i] - 1
                    if cnt == M:
                        idx = i
                        break
                else:
                    idx = i
                    while cntList[i] != 1:
                        cntList[i] -= 1
                        backList.insert(0, 1)
                        cnt += 1
                        if cnt == M:
                            backList.insert(0, cntList[i])
                            break
                    break

    # print(*cntList[idx:])
    print(*cntList[:idx]+backList)


countBead(final)