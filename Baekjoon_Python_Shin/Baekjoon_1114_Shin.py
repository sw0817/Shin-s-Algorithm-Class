# 백준 1114 통나무 자르기
# Baekjoon 1114

# Created by sw0817 on 2021. 08. 09..
# Copyright © 2021 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1114

# 이분탐색을 통해 가장 긴 조각의 길이를 찾을 것.
# 처음 자르는 위치가 작은 것을 찾을 것이므로, 오른쪽부터 잘라서
# 마지막에 자른 위치가 정답이거나, 더 자를 수 있다면 가장 가까운 위치가 답일 것.

def check(m):
    l = L
    cnt = C # 자를 수 있는 횟수
    for i in range(K-1, -1, -1):
        nx = 0 if i == 0 else ks[i-1]
        if l - ks[i] > m:
            return False
        if l - nx > m:
            if cnt == 0:
                return 0
            l = ks[i]
            cnt -= 1
    if l > m:
        return False
    return True


def cut(m):
    cnt = C
    l = L
    for i in range(K-1, -1, -1):
        nx = 0 if i == 0 else ks[i-1]
        if l - nx > m:
            l = ks[i]
            cnt -= 1
    if cnt:
        return ks[0]
    else:
        return l


L, K, C = map(int, input().split())
ks = list(map(int, input().split()))
ks.sort()
start = 0
end = 1000000000
result = end

while start < end:
    mid = (start + end) // 2
    if check(mid):
        end = mid
    else:
        start = mid + 1

print(start, cut(start))