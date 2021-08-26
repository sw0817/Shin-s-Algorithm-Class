import random

# N, M = map(int, input().split())
N, M = random.randint(1, 10), random.randint(1, 10)
if N <= M:
    A = [random.randint(1, 7) for _ in range(N)]
    B = [random.randint(1, 7) for _ in range(M)]
else:
    B = [random.randint(1, 7) for _ in range(N)]
    A = [random.randint(1, 7) for _ in range(M)]
    N, M = M, N
print(N, M)
print(A)
print(B)

if 6 * N < M:
    print(-1)

else:
    between = sum(B) - sum(A)
    reverse = False
    if between < 0:
        reverse = True
    change = [0] * 5
    for n in B:
        continue # 푸는 중
