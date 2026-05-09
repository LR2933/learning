n, m = map(int, input().split())

toys = []
for _ in range(n):
    toward, job = input().split()
    if toward == '0':
        toys.append([1, job])
    else:
        toys.append([-1, job])

index = 0
for _ in range(m):
    a, s = input().split()
    if a == '1':
        toward = 1
    else:
        toward = -1
        
    step = toys[index][0] * toward * int(s) 
    index = (index + step + n) % n

print(toys[index][1])

