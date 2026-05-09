import sys
n = int(sys.stdin.readline().strip())
t = list(map(int, sys.stdin.readline().strip().split()))

data = []
for i, v in enumerate(t, 1):
    data.append((i, v))

data.sort(key = lambda x: x[1])

ps = [0] * (n + 1)
for i in range(n):
    print(data[i][0], end = ' ')
    ps[i + 1] = data[i][1] + ps[i]

print()
print(f"{(sum(ps[:-1])) / n:.2f}")

