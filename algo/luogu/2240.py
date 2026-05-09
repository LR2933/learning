import sys
n, t = map(int, input().strip().split())
data = []
for i in range(n):
    m, v = map(int, sys.stdin.readline().strip().split())
    data.append((m, v))

data.sort(key = lambda x: x[1] / x[0], reverse = True)

value = 0
for m, v in data:
    if t >= m:
        t -= m
        value += v
    else:
        value += t * (v / m)
        break
    
print(f'{value:.2f}')
