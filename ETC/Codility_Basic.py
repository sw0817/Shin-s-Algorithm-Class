value = 12356
bin_value = bin(value)[2:]
print(bin_value)

cnt = 0
cur = 0

for n in bin_value:
    if n == '1':
        cnt = max(cnt, cur)
        cur = 0
    else:
        cur += 1

cnt = max(cnt, cur)
print(cnt)

cnt = 0
i = 0
cur = 0
while 2 ** i <= value:
    if value & (1 << i):
        cnt = max(cnt, cur)
        cur = 0
    else:
        cur += 1
    i += 1
cnt = max(cnt, cur)
print(cnt)