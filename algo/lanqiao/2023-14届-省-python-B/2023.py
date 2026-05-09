def check(n):
    ss = str(n)
    target = '2023'
    idx = 0
    for i in ss:
        if i == target[idx]:
            idx += 1
            if idx == 4:
                return True
    return False

count = 0
for i in range(12345678, 98765432):
    if check(i):
        count += 1

ans = 98765432 - 12345678 + 1 - count
print(ans)



